from playwright.sync_api import sync_playwright
import os
from datetime import datetime
from configparser import ConfigParser
import pytest




def before_all(context):
    context.playwright = sync_playwright().start()
    browser_name = context.config.userdata.get('browser', 'chromium')
    if browser_name == "chromium":
        context.browser = context.playwright.chromium.launch(headless=False)
    elif browser_name == "firefox":
        context.browser = context.playwright.firefox.launch(headless=False)
    elif browser_name == "webkit":
        context.browser = context.playwright.webkit.launch(headless=False)
    elif browser_name == "edge":
        context.browser = context.playwright.chromium.launch(channel="msedge", headless=False)
    elif browser_name == "chrome":
        context.browser = context.playwright.chromium.launch(channel="chrome", headless=False)
    else:
        raise ValueError(f"Unsupported browser: {browser_name}")
    # context.browser = getattr(context.playwright, browser_name).launch(headless=False, slow_mo=1000)

    # Directories for traces, videos, and screenshots

    context.trace_dir = os.path.join(os.getcwd(), "traces")
    context.video_dir = os.path.join(os.getcwd(), "videos")
    context.screenshot_dir = os.path.join(os.getcwd(), "screenshots")
    os.makedirs(context.trace_dir, exist_ok=True)
    os.makedirs(context.video_dir, exist_ok=True)
    os.makedirs(context.screenshot_dir, exist_ok=True)
    os.makedirs('reports', exist_ok=True)

    context.logs = []
    context.scenarios = []
    context.log = lambda message: context.logs.append(f"{datetime.now()}: {message}")
    context.timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")

    config_data = ConfigParser()
    config_data.read("config.ini")
    context.config_data = config_data

browser_context = None

def after_all(context):
    with open('reports/log.txt', 'w') as log_file:
        log_file.write("\n".join(context.logs))
    context.browser.close()
    context.playwright.stop()


def before_scenario(context, scenario):
    width = int(context.config.userdata.get('width', 1280))
    height = int(context.config.userdata.get('height', 720))
    timestamp = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
    video_dir = os.path.join(context.video_dir, f"{scenario.name}_{timestamp}")

    context.browser_context = context.browser.new_context(

        viewport={'width': width, 'height': height},
        record_video_dir=video_dir,
        record_video_size={"width": 1280, "height": 720}
    )
    global browser_context
    browser_context = context.browser_context
    context.page = context.browser_context.new_page()
    print("inside", browser_context)
    context.browser_context.tracing.start(screenshots=True, snapshots=True)


def after_scenario(context, scenario):
    timestamp = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')

    if scenario.status == 'failed':
        screenshot_path = os.path.join(context.screenshot_dir, f"{scenario.name}_{timestamp}.png")
        context.page.screenshot(path=screenshot_path)

    trace_path = os.path.join(context.trace_dir, f"{scenario.name}_{timestamp}.zip")
    context.browser_context.tracing.stop(path=trace_path)

    status = 'passed' if scenario.status == 'passed' else 'failed'
    context.scenarios.append({'name': scenario.name, 'status': status})
    context.log(f"Scenario {scenario.name} finished with status {status}")

    context.page.close()
    context.browser_context.close()
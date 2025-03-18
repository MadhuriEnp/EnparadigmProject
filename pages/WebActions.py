import pandas as pd
from playwright.sync_api import sync_playwright
import pyperclip

import pytesseract
from PIL import Image
import io

class WebActions:
    def __init__(self, page, browser_context):
        self.page = page
        self.page2 = None
        self.page3 = None
        self.browser_context = browser_context


    def move_mouse(self, x, y):
        self.page.mouse.move(x, y)

    def click_mouse(self, x, y):
        self.page.mouse.click(x, y)

    def type_text(self, selector, text):
        element = self.page.locator(selector)
        element.click()
        self.page.keyboard.type(text)

    def goto(self, url:str):
        self.page.goto(url)

    def drag_and_drop(self, source, target):
        self.page.drag_and_drop(source, target)

    def hover_element(self, selector):
        element = self.page.locator(selector)
        element.hover()

    def click(self, selector):
        element = self.page.locator(selector)
        element.click()

    def clear_text_with_backspace(self, selector, num_backspaces=10):
        # Focus on the input field
        self.page.locator(selector).click()

        # Press the backspace key the specified number of times
        for _ in range(num_backspaces):
            self.page.keyboard.press("Backspace")

    def fill(self, locator: str, text: str):
        self.page.locator(locator).fill(text)

    def keyboard_press(self, text:str):
        self.page.keyboard.press(text)
    def dealbtnclick(self):
        self.page.locator("#select2-hk4a-container").click()
        self.page.get_by_role("treeitem", name="testm").click()

    def wait_for_timeout(self, timeout_ms: int):
        print(f"Waiting for {timeout_ms} milliseconds...")
        self.page.wait_for_timeout(timeout_ms)
        print("Wait completed.")

    def elements_count(self, selector):
        elements = self.page.locator(selector).count()
        return elements

    def locator(self, selector):
        self.page.locator(selector)

    def title(self):
        title  = self.page.title()
        return title

    def query_selector_click(self, selector, text):
        select_Dropdown = self.page.query_selector(selector)
        select_Dropdown.select_option(value=text)

    def input_value(self, selector):
        text = self.page.locator(selector).input_value()
        return text

    def get_by_role_get_by_role_click(self, tag1, text1, tag2, text2):
        self.page.get_by_role(tag1,name=text1).get_by_role(tag2, name=text2).click()

    def frame_locator_fill(self, frameSelector, elementSelector, text):
        self.page.frame_locator(frameSelector).locator(elementSelector).fill(text)

    def frame_locator_click(self, frameSelector, elemetSelector):
        self.page.frame_locator(frameSelector).locator(elemetSelector).click()

    def get_by_text_click(self, text:str):
        self.page.get_by_text(text,  exact=True).click()

    def get_by_test_id_by_role_click(self, test_id, tag, text):
        self.page.get_by_test_id(test_id).get_by_role(tag, name=text).click()

    def get_by_placeholder_dbclick(self, placeHldTxt):
        self.page.get_by_placeholder(placeHldTxt).dblclick()

    def get_by_placeholder_fill(self, placeHldTxt, text):
        self.page.get_by_placeholder(placeHldTxt).fill(text)

    def get_by_role_select_option(self, roleTxt, txt):
        self.page.get_by_role(roleTxt).select_option(txt)

    def locator_gettext_click(self, selector, text):
        self.page.locator(selector).get_by_text(text,  exact=True).click()

    def get_by_placeholder_click(self, placeHldTxt):
        self.page.get_by_placeholder(placeHldTxt).click()

    def set_input_files(self, elementSelector, filepath:str):
        self.page.locator(elementSelector).set_input_files(filepath)

    def set_input_files_in_frame(self, frameSelector, elementSelector, filepath:str):
        self.page.frame_locator(frameSelector).locator(elementSelector).set_input_files(filepath)

    def frame_inside_frame_type(self, outerFrameSlector, innerFrameSelector, elementSelector, text):
        self.page.frame_locator(outerFrameSlector).frame_locator(innerFrameSelector).locator(elementSelector).type(text)

    def frame_inside_frame_type_content(self, outerFrameSlector, innerFrameSelector, elementSelector, text):
        self.page.locator(outerFrameSlector).content_frame.locator(
            innerFrameSelector).content_frame.locator(elementSelector).fill(text)

    #def click_button_in_iframe(self, iframe_selector: str, button_role: str, button_name: str):
    #     self.page.locator(iframe_selector).content_frame().get_by_role(button_role, name=button_name).click()

    def click_button_in_iframe(self):
        self.page.locator("[data-testid=\"video-scenario-iframe\"]").content_frame.get_by_role("button",name="Upload Video").click()

    def video1upload(self,framelocator,contentframelocator,filename):
        self.page.locator(framelocator).content_frame.locator(contentframelocator).filter(
            has_text="Video 1 Remove Video File").get_by_label("Video File").set_input_files(filename)

    def video2upload(self, framelocator, contentframelocator, filename):
        self.page.locator(framelocator).content_frame.locator(contentframelocator).filter(
            has_text="Video 2 Remove Video File").get_by_label("Video File").set_input_files(filename)

    def video2upload(self):
        self.page.locator("#iFrameResizer0").content_frame.locator("form div").filter(has_text="Video 2 Remove Video File").get_by_label("Video File").set_input_files("VideoRefName.mp4")

    def text_content(self, selector):
        text = self.page.locator(selector).text_content()
        return text

    def get_by_role(self, tag:str, nameTxt:str):
        self.page.get_by_role(tag, name=nameTxt).click()

    def assertValues(self, actualValue:str, expectValue:str):
        assert expectValue == actualValue, f"Expected message '{expectValue}' but got '{actualValue}'"
        print("Actual value", actualValue)
        print("Expect value", expectValue)

    def wait_for_selector(self, selector,  num:int):
        self.page.wait_for_selector(selector, timeout=num)

    def reload(self):
        self.page.reload()

    def is_visible(self, selector, selectorTxt):
        element = self.page.locator(selector)  # Replace with actual selector
        if element.is_visible():
            print(f"{selectorTxt}Element is visible")

    def frame_locator_loc_is_visible(self, frameselector, elelocator, selectorTxt):
        element = self.page.frame_locator(frameselector).locator(elelocator).is_visible()
        if element.is_visible():
            print(f"{selectorTxt}Element is visible")

    def frame_inside_frame_loc_is_visible(self,  frameselector1, frameselector2, elelocator, selectorTxt):
        element = self.page.frame_locator(frameselector1).frame_locator(frameselector2).locator(elelocator).is_visible()
        if element.is_visible():
            print(f"{selectorTxt}Element is visible")

    def is_enabled(self,selector):
        locator = self.page.locator(selector)

        if locator.is_enabled():
            print(f"{selector} is enabled.")
        else:
            print(f"{selector} is disabled.")

    def is_disabled(self,selector):
        locator = self.page.locator(selector)

        if locator.is_disabled():
            print(f"{selector} is disabled.")
        else:
            print(f"{selector} is enabled.")

    def select_option_visible_text(self, dropdownSelector, text):
        self.page.select_option(dropdownSelector, label=text)

    def select_option_value(self, dropdownSelector, value):
        self.page.select_option(dropdownSelector,
            value=value)

    def get_by_role_nth_select_option(self, selector, role, num, opt):
        self.page.locator(selector).get_by_role(role).nth(num).select_option(opt)

    def openNewTab1(self):
        self.page2 = self.browser_context.new_page()

    def open_url_in_newTab1(self, link):
        self.page2.goto(link)

    def url(self):
        url = self.page.url()
        return url

    def go_back(self):
        self.page.go_back()

    def locator_first_click(self, selector):
        self.page.locator(selector).first.click()

    def newTab1_get_by_role(self, tag:str, nameTxt:str):
        self.page2.get_by_role(tag, name=nameTxt).click()

    def newTab1_get_by_role_is_visible(self, tag, text):
        self.page2.get_by_role(tag, name=text).is_visible()

    def newTab1_get_by_role_dbclick(self, tag, text):
        self.page2.get_by_role(tag, name=text).dblclick()

    def newTab1_locator_get_by_role(self, selector,tag, text):
        self.page2.locator(selector).get_by_role(tag, name=text).click()

    def newTab1_get_by_role_nth_text_content(self, tag, text, selector, num):
        text = self.page2.get_by_role(tag, name=text).locator(selector).nth(num).text_content()
        return text


    def newTabAfterClickingAnElement(self, selector):
        with self.page.expect_popup() as page2_info:
            self.page.click(selector)
        self.page2 = page2_info.value

    def newTab1_elements_count(self, selector):
        elements = self.page2.locator(selector).count()
        return elements

    def newTabAfterClickingAnElementWhichIsInFrame(self, frameSlector, text):
        with self.page.expect_popup() as page2_info:
            self.page.frame_locator(frameSlector).get_by_label(
                text).click()
        self.page2 = page2_info.value

    def new_tab1_get_by_label_fill(self, text, selector):
        self.page2.get_by_label(text).fill(selector)

    def newTab1Click(self,selector):
        self.page2.click(selector)

    def newTab1_after_get_by_role_get_by_role_click(self, tag1, text1, tag2, text2):
        with self.page.expect_popup() as page2_info:
            self.page.get_by_role(tag1,name=text1).get_by_role(tag2, name=text2).click()
        self.page2 = page2_info.value

    def newTab1Fill(self, selector, text):
        self.page2.fill(selector, text)

    def newTab1_dbclick(self, selector):
        self.page2.dblclick(selector)

    def newTab1WaitForTimeout(self, timeout_ms: int):
        print(f"Waiting for {timeout_ms} milliseconds...")
        self.page2.wait_for_timeout(timeout_ms)
        print("Wait completed.")

    def newTab1_get_by_placeholder_fill(self, placeHldTxt, text):
        self.page2.get_by_placeholder(placeHldTxt).fill(text)

    def newTab1_get_by_placeholder_click(self, placeHldTxt):
        self.page2.get_by_placeholder(placeHldTxt).click()

    def newTab1_get_by_text_is_visible(self,text):
        self.page2.get_by_text(text).is_visible()

    def newTab1TextContent(self, selector):
        text = self.page2.locator(selector).text_content()
        return text

    def newTab1GetByTextFirstClick(self, text):
        self.page2.get_by_text(text).first.click()

    def newTab1GetByTextClick(self, text):
        self.page2.get_by_text(text,  exact=True).click()

    def newTab1_after_clicking_frame_get_by_role(self, framelocator, tag, text):
        with self.page.expect_popup() as page2_info:
            self.page.frame_locator(framelocator).get_by_role(tag,name=text).click()
        self.page2 = page2_info.value

    def newTab1_locator_filter_has_text_first_click(self, selector, num):
        self.page2.locator(selector).filter(has_text=num).first.click()

    def newTab1_locator_first_click(self, selector):
        self.page2.locator(selector).first.click()

    def newTab1GetByTextLastClick(self, text):
        self.page2.get_by_text(text).last.click()

    def newTab1GetByTextNthClick(self,text, num):
        self.page2.get_by_text(text,  exact=True).nth(num).click()

    def newTab1_get_attribute(self, selector, key):
        text = self.page2.locator(selector).get_attribute(key)
        return text

    def newTab1isEnabled(self,selector, selText):
        locator = self.page2.locator(selector)
        locator.is_enabled()
        print(f"{selText} is enabled.")

    def newTab1isDisabled(self,selector, selText):
        locator = self.page2.locator(selector)
        locator.is_disabled()
        print(f"{selText} is disabled.")

    def newTab1_get_by_role_nth_click(self, tag, text, num):
        self.page2.get_by_role(tag, name=text).nth(num).click()


    def newTab1_mouse_hover_get_text(self, hover_selector, text_selector, hover_selector_text):
        self.page2.locator(hover_selector).hover()
        self.page2.wait_for_selector(text_selector, timeout=1000)
        hover_text = self.page2.locator(text_selector).inner_text()
        print(f"{hover_selector_text} Hover Text:", hover_text)
        return hover_text

    def newTab1_is_visible(self, selector, selectorTxt):
        element = self.page2.locator(selector)  # Replace with actual selector
        if element.is_visible():
            print(f"{selectorTxt}Element is visible")

    def newTab1_frame_locator_fill(self, frameSelector, elementSelector, text):
        self.page2.frame_locator(frameSelector).locator(elementSelector).fill(text)

    def newTab1_set_input_files_in_frame(self, frameSelector, elementSelector, filepath:str):
        self.page2.frame_locator(frameSelector).locator(elementSelector).set_input_files(filepath)

    def click_link_open_new_tab_coping(self, selector):
        self.page.click(selector)
        copied_link = pyperclip.paste()
        self.page2 = self.browser_context.new_page()
        self.page2.goto(copied_link)

    def opening_browse_context_newTab1(self):
        self.page2 = self.browser_context.new_page()

    def goto_newtab2_by_clicking_element(self, selector):
        with self.page2.expect_popup() as page3_info:
            self.page2.click(selector)
        self.page3 = page3_info.value

    def new_tab2_wait_for_timeout(self, num:int):
        self.page3.wait_for_timeout(num)

    def new_tab2_text_content(self, selector):
        text = self.page3.locator(selector).text_content()
        return text

    def clear_text_field(self, selector):
        self.page.locator(selector).fill("")

    def get_data_by_excel_file(self, file_path, sheet_name, rowNum:int, colNum:int):
        df = pd.read_excel(file_path, sheet_name=sheet_name, engine="openpyxl")
        cell_value = df.iloc[rowNum, colNum]
        return cell_value

    def getCanvasText(self):
        canvas_image = self.page.locator("//div[@class='w-full h-full']//canvas").screenshot()
        print("Captured Canvas Image:", canvas_image)
        return canvas_image

    def captureTextFromCanvas(self):
        # Convert the image bytes into a PIL Image object
        image = Image.open(io.BytesIO(self.getCanvasText()))
        # Use Tesseract to extract text from the image
        extracted_text = pytesseract.image_to_string(image)
        print("Captured Canvas Image:", self.getCanvasText())
        print("Extracted Text:", extracted_text)

        return extracted_text



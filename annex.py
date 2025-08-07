with SB(uc=True, test=True) as xzfaeqa:

    url = "https://kick.com/brutalles"
    xzfaeqa.uc_open_with_reconnect(url, 4)
    xzfaeqa.sleep(4)
    xzfaeqa.uc_gui_click_captcha()
    xzfaeqa.sleep(1)
    xzfaeqa.uc_gui_handle_captcha()
    xzfaeqa.sleep(4)
    if xzfaeqa.is_element_present('button:contains("Accept")'):
        xzfaeqa.uc_click('button:contains("Accept")', reconnect_time=4)
    if xzfaeqa.is_element_visible('#injected-channel-player'):
        xzfaeqa2 = xzfaeqa.get_new_driver(undetectable=True)
        xzfaeqa2.uc_open_with_reconnect(url, 5)
        xzfaeqa2.uc_gui_click_captcha()
        xzfaeqa2.uc_gui_handle_captcha()
        xzfaeqa.sleep(10)
        if xzfaeqa2.is_element_present('button:contains("Accept")'):
            xzfaeqa2.uc_click('button:contains("Accept")', reconnect_time=4)
        while xzfaeqa.is_element_visible('#injected-channel-player'):
            xzfaeqa.sleep(10)
        xzfaeqa.quit_extra_driver()
    xzfaeqa.sleep(1)

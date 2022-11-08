from pages.base_page import BasePage


class MatchForm(BasePage):
    button_main_page_xpath = "//div/span[@class='MuiTouchRipple-root']"
    button_players_xpath = "//div[2][@class='MuiButtonBase-root MuiListItem-root MuiListItem-gutters MuiListItem-button']"
    players_count_xpath = "//div[text()='Players count']"
    matches_count_xpath = "//div[text()='Matches count']"
    reports_count_xpath = "//div[text()='Reports count']"
    events_count_xpath = "//div[text()='Events count']"
    button_change_language_xpath = "/div[@class='MuiListItemText-root']"
    button_sign_out_xpath = "//span[text()='Sign out']"
    shortcuts_xpath = "//h2[text()='Shortcuts']"
    activity_xpath = "//h2[text()='Activity']"







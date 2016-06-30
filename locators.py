from selenium.webdriver.common.by import By


# for maintainability we can seperate web objects by page name

class MainPageLocatars(object):
    LOGO = (By.CSS_SELECTOR, '.logo-lg>img')
    ACCOUNT = (By.ID, 'nav-link-yourAccount')
    SIGNUP = (By.CSS_SELECTOR, '#nav-flyout-ya-newCust > a')
    LOGIN = (By.CSS_SELECTOR, '#nav-flyout-ya-signin > a')
    SEARCH = (By.ID, 'twotabsearchtextbox')
    SEARCH_LIST = (By.ID, 's-results-list-atf')


class LoginPageLocatars(object):
    EMAIL = (By.ID, 'Email')
    PASSWORD = (By.ID, 'Password')
    SUBMIT = (By.CSS_SELECTOR, '.btn.btn-primary')
    PASSWORD_ERROR_MESSAGE = (By.ID, 'Password_error')
    EMAIL_ERROR_MESSAGE = (By.ID, 'Email_error')

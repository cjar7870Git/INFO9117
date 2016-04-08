from behave import *
import re
@given ("at the register screen")
def step_impl(context):
    context.browser.get(context.address + "/register")
    register_found = re.search("register", context.browser.page_source, re.IGNORECASE)
    assert register_found

@when("a new user submits their unique {username} and {password}")
def step_impl(context, username, password):
    """
    :type context: behave.runner.Context
    :type username: str
    :type password: str
    """
    submit_username_password(context, username, password)

@then ("the system should record the {username} and {password} of the new user")








def submit_username_password(context, username, password):
    username_field = context.browser.find_element_by_name("username")
    password_field = context.browser.find_element_by_name("password")
    username_field.send_keys(username)
    password_field.send_keys(password)
    username_field.submit()
    context.response = context.browser.page_source


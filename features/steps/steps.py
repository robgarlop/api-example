from behave import *
from requests import *


@given('I set base url to "{url}"')
def step_impl(context, url):
    context.base_url = url


@when('I retrieve info of the pet with ID "{id}"')
def step_impl(context, id):
    context.r = request("GET", context.base_url + id, verify=False)


@then('I should get status code "{code}"')
def step_impl(context, code):
    assert context.r.status_code == int(code)


@step('The name should be "{text}"')
def step_impl(context, text):
    assert context.r.json()['name'] == text, "Current: " + context.r.json()['name'] + " Expected: " + text
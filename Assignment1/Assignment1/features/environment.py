from selenium import webdriver
import threading
import Assignment1

def before_all(ctx):
    ctx.server = Assignment1
    ctx.address = Assignment1.address
    ctx.thread = threading.Thread(target=ctx.server.serve_forever)
    ctx.thread.start()  # start flask app server
    ctx.browser = webdriver.Firefox()

def after_all(ctx):
    ctx.browser.get(ctx.address + "/shutdown") # shut down flask app server
    ctx.thread.join()
    ctx.browser.quit()

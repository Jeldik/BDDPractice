from Common.CommonFuncs import webcommon


def before_scenario(context, scenario):
    context.driver = webcommon.open_browser(context.config.userdata.get("browser"))


def after_step(context, step):
    if step.status.name == 'failed':
        # take screen shot
        pass

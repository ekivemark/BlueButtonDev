"""
bluebuttondev.bbdev
FILE: utils
Created: 6/16/15 12:11 AM
Basic conversion tools
"""
__author__ = 'Mark Scrimshire:@ekivemark'

def str2int(inp):
    output = 0 + int(inp)

    return output


def str2bool(inp):
    output = False
    if inp.upper() == "TRUE":
        output = True
    elif inp.upper() == "FALSE":
        output = False

    return output


def email_domain(email, at=False):
    # get email domain from an email field.
    if at == False:
        return email.split('@')[1].rstrip()
    else:
        # include the @
        return "@" + email.split('@')[1].rstrip()


def email_name(email, at=False):
    # get email username from an email field.
    if at == False:
        return email.split('@')[0].rstrip()
    else:
        # include the @
        return email.split('@')[0].rstrip()+"@"


def email_mask(email=""):
    """
    mask and potentially shorten an email address
    Useful for communications
    :param email:
    :return:
    """

    if email=="":
        return None

    domain = "@"+email.split("@")[1]
    tld    = "."+domain.split(".")[1]

    if settings.DEBUG:
        print("Domain:",domain)

    result_email = email[:2]+"**" + domain[:2] + "**" + tld[:2] + "**"

    return result_email
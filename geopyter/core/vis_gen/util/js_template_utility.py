def append_div(uuid):
    return (
        "if (document.getElementById('" + uuid + "') === null)"
        "  element.append($('<div/>', {id:'" + uuid + "'}));"
    )
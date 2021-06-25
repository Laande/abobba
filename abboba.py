# ---------------------------

# Character

INVISIBLE = "char"  # change this string with an invisible character

# Command

CMD = "!ab"

# ---------------------------

import sys
from g_python.gextension import Extension
from g_python.hmessage import Direction


extension_info = {
    "title": "Anti Bobba",
    "description": CMD + " on/off",
    "version": "2.0",
    "author": "Lande"
}

ext = Extension(extension_info, sys.argv)
ext.start()


on = False


def speech(msg):
    global on

    (text, bubble, idd) = msg.packet.read('sii')

    if on:
        if not text.startswith(CMD):
            msg.is_blocked = True
            message = ""

            for i in text:
                message += i + INVISIBLE

            ext.send_to_server('{out:Chat}{s:"%s"}{i:%s}{i:%s}' % (message, bubble, idd))

    if text == CMD + " on":
        msg.is_blocked = True
        on = True
        ext.write_to_console('Anti Bobba on')

    if text == CMD + " off":
        msg.is_blocked = True
        on = False
        ext.write_to_console('Anti Bobba off')


ext.intercept(Direction.TO_SERVER, speech, 'Chat')

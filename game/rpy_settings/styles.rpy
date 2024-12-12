init python:
    def thoughts_tag(tag, argument, contents):
        size = 22

        return [
                (renpy.TEXT_TAG, u"size={}".format(size)),
                (renpy.TEXT_TAG, u"i"),
            ] + contents + [
                (renpy.TEXT_TAG, u"/size"),
                (renpy.TEXT_TAG, u"/i"),
            ]

    config.custom_text_tags["thoughts"] = thoughts_tag
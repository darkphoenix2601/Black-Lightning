"""Emoji

Available Commands:

.box
.lefft
.up
.circle
.dill
.repee
.fairnhansome"""

import asyncio


@borg.on(admin_cmd(pattern="box ?(.*)", outgoing=True))
async def _(event):

    if event.fwd_from:

        return

    animation_interval = 0.1

    animation_ttl = range(0, 100)

    input_str = event.pattern_match.group(1)

    if input_str == "load":

        await event.edit(input_str)

        animation_chars = ["▮", "▯", "▬", "▭" "‎"]

        for i in animation_ttl:

            await asyncio.sleep(animation_interval)

            await event.edit(animation_chars[i % 4])


import asyncio


@borg.on(admin_cmd(pattern="lefft ?(.*)", outgoing=True))
async def _(event):

    if event.fwd_from:

        return

    animation_interval = 0.1

    animation_ttl = range(0, 100)

    input_str = event.pattern_match.group(1)

    if input_str == "square":

        await event.edit(input_str)

        animation_chars = ["◧", "◨", "◧", "◨" "‎"]

        for i in animation_ttl:

            await asyncio.sleep(animation_interval)

            await event.edit(animation_chars[i % 4])


@borg.on(admin_cmd(pattern="up ?(.*)", outgoing=True))
async def _(event):

    if event.fwd_from:

        return

    animation_interval = 0.1

    animation_ttl = range(0, 100)

    input_str = event.pattern_match.group(1)

    if input_str == "up":

        await event.edit(input_str)

        animation_chars = ["╹", "╻", "╹", "╻" "‎"]

        for i in animation_ttl:

            await asyncio.sleep(animation_interval)

            await event.edit(animation_chars[i % 4])


@borg.on(admin_cmd(pattern="circle ?(.*)", outgoing=True))
async def _(event):

    if event.fwd_from:

        return

    animation_interval = 0.1

    animation_ttl = range(0, 100)

    input_str = event.pattern_match.group(1)

    if input_str == "round":

        await event.edit(input_str)

        animation_chars = ["⚫", "⬤", "●", "∘" "‎"]

        for i in animation_ttl:

            await asyncio.sleep(animation_interval)

            await event.edit(animation_chars[i % 4])


@borg.on(admin_cmd(pattern="dill ?(.*)", outgoing=True))
async def _(event):

    if event.fwd_from:

        return

    animation_interval = 0.1

    animation_ttl = range(0, 100)

    input_str = event.pattern_match.group(1)

    if input_str == "heart":

        await event.edit(input_str)

        animation_chars = ["🖤", "❤️", "🖤", "❤️" "‎"]

        for i in animation_ttl:

            await asyncio.sleep(animation_interval)

            await event.edit(animation_chars[i % 4])


@borg.on(admin_cmd(pattern="repee ?(.*)", outgoing=True))
async def _(event):

    if event.fwd_from:

        return

    animation_interval = 1

    animation_ttl = range(0, 11)

    input_str = event.pattern_match.group(1)

    if input_str == "anim":

        await event.edit(input_str)

        animation_chars = [
            "😁",
            "😧",
            "😡",
            "😢",
            "‎**Repo by @r4v4n4**",
            "😁",
            "😧",
            "😡",
            "😢",
            "‎github.com/ravana69/pornhub",
            "__**RePe GeNg Is BeHiNd You....**__",
        ]

        for i in animation_ttl:

            await asyncio.sleep(animation_interval)

            await event.edit(animation_chars[i % 11])


@borg.on(admin_cmd(pattern="fairnhansome ?(.*)", outgoing=True))
async def _(event):

    if event.fwd_from:

        return

    animation_interval = 2

    animation_ttl = range(0, 6)

    input_str = event.pattern_match.group(1)

    if input_str == "fnl":

        await event.edit(input_str)

        animation_chars = [
            "😁🏿",
            "😁🏾",
            "😁🏽",
            "😁🏼",
            "‎😁",
            "**Fair & Lovely GeNg Is BeHiNd You....**",
        ]

        for i in animation_ttl:

            await asyncio.sleep(animation_interval)

            await event.edit(animation_chars[i % 6])

import aiohttp
from pyrogram import Client
from misskaty import app
from misskaty.ultis_ex.wmilia_m.decorators import *

@usage("/pokedex [pokemon name]")
@example("/pokedex pikachu")
@description(
    "This works like a real pokedex and it will send you information regarding a specific pokemon."
)
@app.on_message(filters.command(commands="pokedex", disable=True))
async def PokeDex(_, message):
    if len(message.text.split()) != 2:
        await usage_string(message, PokeDex)
        return

    pokemon = message.text.split(None, 1)[1]
    pokedex_url = f"https://pokeapi.co/api/v2/pokemon/{pokemon}"

    async with aiohttp.ClientSession() as session:
        async with session.get(pokedex_url) as request:
            if request.status == 404:
                return await message.reply_text("Wrong Pokemon Name.")
            result = await request.json()

            try:
                pokemon_name = result["name"]
                pokedex_id = result["id"]
                types = ", ".join(typo["type"]["name"] for typo in result["types"][:5])
                abilities = ", ".join(ability["ability"]["name"] for ability in result["abilities"][:5])
                height = result["height"]
                weight = result["weight"]
                stats = "\n".join(f"{stat['stat']['name']}: {stat['base_stat']}" for stat in result["stats"])

                caption = f"""**Pokemon:** `{pokemon_name}`
**Pokedex:** `{pokedex_id}`
**Type:** `{types}`
**Abilities:** `{abilities}`
**Height:** `{height}`
**Weight:** `{weight}`
**Stats:**
{stats}
"""
            except Exception as e:
                print(str(e))

    poke_img = f"https://img.pokemondb.net/artwork/large/{pokemon_name}.jpg" if "pokemon_name" in locals() else None

    if poke_img:
        await message.reply_photo(photo=poke_img, caption=caption)
    else:
        await message.reply_text(caption)

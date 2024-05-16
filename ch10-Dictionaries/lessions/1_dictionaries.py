def get_character_record(name, server, level, rank):
    return {"id":f"{name}#{server}",
            "name":name,
            "server":server,
            "level":level,
            "rank":rank
            }

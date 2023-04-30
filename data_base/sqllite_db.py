import sqlite3 as sq
from create_bot import bot

def sql_start():
    global dbase, cur
    dbase = sq.connect('elis_gallery.db')
    cur = dbase.cursor()
    if dbase:
        print('Data base connected Ok!')
    dbase.execute('create table if not exists gallery(img TEXT, name TEXT primary key, description TEXT, price TEXT)')
    dbase.commit()

async def sql_add_command(state):
    async with state.proxy() as data:
        cur.execute('insert into gallery values (?,?,?,?)', tuple(data.values()))
        dbase.commit()

async def sql_read(message):
    for ret in cur.execute('select * from gallery').fetchall():
        await bot.send_photo(message.from_user.id, ret[0], f'{ret[1]}\n Description: {ret[2]}\nPrice {ret[-1]}')

async def sql_read2():
    return cur.execute('select * from gallery').fetchall()

async def sql_delete_command(data):
    cur.execute('delete from gallery where name == ?', (data,))
    dbase.commit()
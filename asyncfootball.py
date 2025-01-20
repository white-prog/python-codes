import time
import asyncio

def shooting_game(person):
    print(f"{person} is shooting ball")
    time.sleep(2)
    print(f"{person} shooted")
async def shooting_gm(person):
    print(f"{person} is shooting ball")
    await asyncio.sleep(2)
    print(f"{person} shooted")




"""
def main():
    persons = ["messi","cristiano","Lewandowski","Rodri","Vinicius","neymar"]
    #synchronous => one after one
    for person in persons:
        shooting_game(person)
"""
#"""
async def mn():
    persons = ["messi","cristiano","Lewandowski","Rodri","Vinicius","neymar"]
    #asynchronous => online ticket booking or shooting everyone at same time to same post
    tasks = [shooting_gm(pers) for pers in persons]
    await asyncio.gather(*tasks)
asyncio.run(mn())
#"""
"""
if __name__ == "__main__":
    main()
"""



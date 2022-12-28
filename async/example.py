import asyncio
import  time


#basic Syc tsak 

def fun1():
    print("This is Function 1")
    time.sleep(10)
    fun3()


def fun2():
    print("This is Function 2")


def fun3():
    print("This is Function 3")


fun1()


#Second Example

async def task1():
    print("Send First Email -")
    asyncio.create_task(task2())    
    await asyncio.sleep(5)
    print("First Email Reply ")



async def task2():
    print("Send Second Email -")
    asyncio.create_task(task3())
    await asyncio.sleep(3)
    print("Second Email Reply ")


async def task3():
    print("Send Thired Email -")
    await asyncio.sleep(1)
    print("Thired Email Reply ")

asyncio.run(task1())   #run async func 




#using async

async  def file_reply():
    await asyncio.sleep(5)
    return {'file_Size':"100Kb"}



async  def showfile():
    print("Waiting for file Size :")
    x = await file_reply()
    print("This is File Size " , x)



asyncio.run(showfile())



#run parallel  async functions

async  def file_reply():
    await asyncio.sleep(5)
    return {'file_Size':"100Kb"}

async  def data_reply():
    await asyncio.sleep(5)
    return {'data':500}


async  def showfile(ty):
    print("Waiting for file Size :",ty)
    
    x = await file_reply()
    print("This is File Size " , x)

    
async  def showdata():
    print("Waiting for Data :")
    x = await data_reply()
    print("This is data value : " , x)


asyncio.run(showfile()) 
async def main():
    files  = asyncio.create_task(showfile("MP3"))
    data  = asyncio.create_task(showdata())
    await files
    await data

asyncio.run(main())











'''task 1 - print - t2 , t1, t3'''

async def t1():
   
    await t2()
    print("t1")

async def t2():
    print("t2")



async def t3():
    await t1()
    print("t3")

asyncio.run(t3())




#task 2 

async def mytask():
    await asyncio.sleep(2)
    print("Hello This is My task ---")
    

async def fatch_data():
    print("Fatching the data : --")
    await asyncio.sleep(5)
    await gen_data()



async def gen_data():
    for i in range(1,10):
        print(i)
        await asyncio.sleep(3)



async def main():
    t1 = asyncio.create_task(fatch_data())
    t2 = asyncio.create_task(mytask())
    await t1
    await t2

asyncio.run(main())
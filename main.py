# from dotenv import load_dotenv
# from prisma import Prisma
# import asyncio
# from flask import jsonify

# from app import create_app

# app = create_app()

# @app.route("/", methods=["GET"])
# async def home():
#     prisma=Prisma()
#     try:
#         await prisma.connect()

#         student=await prisma.student.find_first()

#         return jsonify(student.model_dump())
    
#     finally:
#         prisma.disconnect()



# if __name__=="__main__":
#     app.run(debug=True)

from flask import Flask, jsonify
from prisma import Prisma

app=Flask(__name__)

@app.route("/student", methods=["GET"])
async def list_students():
    prisma=Prisma()
    await prisma.connect()

    student=await prisma.student.find_first(include={
        "parent":True
    })

    student_dict=student.model_dump()
    prisma.disconnect()
    return jsonify (student_dict), 200


if __name__=="__main__":
    app.run(debug=True)
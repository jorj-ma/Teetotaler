from flask import jsonify, Blueprint, request
from app.bcrypt import bcrypt
from prisma import Prisma

auth_bp = Blueprint("auth_bp", __name__)

# JWT ->
#

@auth_bp.route('/login', methods=["POST"])
def login():
    return "login success"

@auth_bp.route('/sign-up', methods=["POST"])
async def sign_up():
    prisma = Prisma()
    await prisma.connect()
    
    try:
        data = request.get_json()
        print("Request body ", data)

        name = data.get("name")
        email = data.get("email")
        password = data.get("password")

        # Validation logic
        if not name:
            return jsonify({"custom": True, "_message": "Name required"}), 400
        
        if not email:
            return jsonify({"custom": True, "_message": "Email required"}), 400
        
        if not password:
            return jsonify({"custom": True, "_message": "Password required"}), 400

        # Strong password check (at least 4 characters)
        if len(password) < 4:
            return jsonify({"custom": True, "_message": "Password must have atleast 4 charcters"}), 400

        # Password hashing
        hashed_password = bcrypt.generate_password_hash(password).decode("utf-8")

        # Logging for debugging
        print("User email is", email)
        print("User password is", password)
        print("User name is", name)
        print("Password hash", hashed_password)

        # Check if email is already in use
        player_exists = await prisma.player.find_unique(
            where={
                "email": email
            }
        )

        if player_exists:
            return jsonify({"custom": True, "_message": "Email already in use."}), 400

        # Money 5000 A to person B
        # A -> subtract 5000
        # B -> Add 5000 acount

        transaction = None

        # Execute database entries within a transaction
        async with prisma.tx() as tx:
            # Create the player
            new_player = await tx.player.create(
                data={
                    "name": name,
                    "email": email
                }
            )

            # Create the associated password entry
            new_player_pass = await tx.player_password.create(
                data={
                    "player_id": new_player.id,
                    "password": hashed_password
                }
            )

            transaction = new_player

        return jsonify(transaction.model_dump())

    except Exception as e:
        print(f"Error during sign-up: {e}")
        return jsonify({"error": str(e)}), 500
    
    finally:
        await prisma.disconnect()
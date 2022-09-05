from app import create_app

if __name__ == "__main__":  # Protect this code to be ran if he is imported
	create_app().run(port=5000, debug=True)

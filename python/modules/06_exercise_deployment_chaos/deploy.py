import sys
import os
import random
import dotenv

dotenv.load_dotenv()

if len(sys.argv) < 2:
    print("no args provided")
    sys.exit(1)

# isProd = False
# if "--prod" in sys.argv:
#     isProd = True

isProd = "--prod" in sys.argv
print(sys.argv)

api_key = os.getenv('API_KEY')

if not api_key:
    print("MISSING KEYS!")

network_instablity = random.randint(1, 100)
if isProd:
    print("Initiating production deployment...")
    if(network_instablity > 75):
        print("FATAL: Deployment failed due to network timeout.")
        sys.exit(1)
    else:
        print("deployed successfully")
else: 
    print("Running dry-run/staging deployment. Skipping network simulation.")



from datetime import datetime

# add more parameters to the definitioin
def run_calculations(method: str) -> None:   
    print("Running calculations")
    method = method.lower()
    start_time = datetime.now()
    print(f"xd: {method}")

    if method == "select best":
        for i in range(10):
            print('Best')
    elif method == "roulette":
        for i in range(10):
            print('Roulette')
    elif method == "tournament":
        for i in range(10):
            print('Tournament')

    end_time = datetime.now()

    print(end_time - start_time)


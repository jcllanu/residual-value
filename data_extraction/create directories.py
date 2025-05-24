import os
makes=["acura","audi","bmw","buick","cadillac","chevrolet","chrysler","dodge","ford","gmc","honda","hyundai","infiniti","jeep","kia","land_rover","lexus",
            "lincoln","mazda","mercedes_benz","mini","mitsubishi","nissan","porsche","ram","subaru","tesla","toyota","volkswagen","volvo"]
for make in makes:
    if not os.path.exists("cars\\"+make):
        os.makedirs("cars\\"+make)
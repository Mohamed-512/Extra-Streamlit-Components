import os

modules = os.listdir("extra_streamlit_components")

for module in modules:
    path = os.path.join("extra_streamlit_components", module, "frontend")
    if os.path.exists(path):
        print(f"Preparing {path}")
        os.system(f"cd {path} && npm i && npm run build")

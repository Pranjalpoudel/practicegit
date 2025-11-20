import os

print("🚀 NUKING AND RECREATING...")

# Force delete and recreate
os.system('rmdir /s /q src 2>nul')

# Create fresh
os.makedirs("src/practicegit/components", exist_ok=True)
os.makedirs("src/practicegit/pipelines", exist_ok=True)

files = [
    "src/practicegit/__init__.py",
    "src/practicegit/components/__init__.py",
    "src/practicegit/components/data_ingestion.py",
    "src/practicegit/components/data_transformation.py", 
    "src/practicegit/components/model_trainer.py",
    "src/practicegit/components/model_monitoring.py",
    "src/practicegit/pipelines/__init__.py",
    "src/practicegit/pipelines/training_pipeline.py",
    "src/practicegit/pipelines/prediction_pipeline.py",
    "src/practicegit/exception.py",
    "src/practicegit/logger.py",
    "src/practicegit/utils.py",
]

for file in files:
    open(file, 'w').close()
    print(f"✅ {file}")

print("🎉 DONE!")
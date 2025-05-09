# Make and activate conda environment
conda env create -f environment.yml
conda activate zero_to_ai_environment

# Get spacy model
python -m spacy download en_core_web_lg

# Run tests
pytest
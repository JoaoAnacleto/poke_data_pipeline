import os
import sys
import pandas as pd
import pytest
from unittest.mock import Mock
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from src.transformer import DataTransformer



def test_categorize_experience():
    # Test categorization of Pokemon experience
    test_data = {
        'Base Experience': [45, 75, 120],
        'Name': ['Pikachu', 'Bulbasaur', 'Charizard']
    }
    df = pd.DataFrame(test_data)
    
    transformer = DataTransformer(Mock())
    result_df = transformer.categorize_experience(df)
    
    # Verify experience categories
    assert result_df['Category'][0] == 'Weak'
    assert result_df['Category'][1] == 'Medium'
    assert result_df['Category'][2] == 'Strong'
    
    # Verify original data is preserved
    assert result_df['Base Experience'][0] == 45
    assert result_df['Base Experience'][1] == 75
    assert result_df['Base Experience'][2] == 120

def test_count_pokemon_by_type():
    # Test counting Pokemon by type
    test_data = {
        'Name': ['Pikachu', 'Bulbasaur', 'Charizard', 'Squirtle'],
        'Types': [['Electric'], ['Grass', 'Poison'], ['Fire', 'Flying'], ['Water']]
    }
    df = pd.DataFrame(test_data)
    
    transformer = DataTransformer(Mock())
    result_df = transformer.count_pokemon_by_type(df)
    
    # Verify type counts
    assert len(result_df) == 6  # 6 unique types
    assert result_df[result_df['Type'] == 'Electric']['Count'].values[0] == 1
    assert result_df[result_df['Type'] == 'Grass']['Count'].values[0] == 1
    assert result_df[result_df['Type'] == 'Poison']['Count'].values[0] == 1
    assert result_df[result_df['Type'] == 'Fire']['Count'].values[0] == 1
    assert result_df[result_df['Type'] == 'Flying']['Count'].values[0] == 1
    assert result_df[result_df['Type'] == 'Water']['Count'].values[0] == 1

def test_transform_pokemon_data():
    # Test complete transformation pipeline
    test_data = {
        'Name': ['Pikachu', 'Bulbasaur', 'Charizard', 'Squirtle', 'Pidgey'],
        'Base Experience': [112, 64, 240, 63, 50],
        'Types': [['Electric'], ['Grass', 'Poison'], ['Fire', 'Flying'], ['Water'], ['Flying']],
        'HP': [35, 45, 78, 44, 40],
        'Attack': [55, 65, 84, 50, 45],
        'Defense': [40, 65, 78, 64, 40]
    }
    df = pd.DataFrame(test_data)
    
    transformer = DataTransformer(Mock())
    result = transformer.transform_pokemon_data(df)
    
    # Verify results
    _, types_df, _, top_df = result
    
    # Verify type counts
    assert len(types_df) == 6
    assert types_df[types_df['Type'] == 'Flying']['Count'].values[0] == 2
    
    # Verify top Pokemon
    assert len(top_df) == 5
    assert top_df.iloc[0]['Name'] == 'Charizard'
    assert top_df.iloc[0]['Base Experience'] == 240

if __name__ == "__main__":
    pytest.main()

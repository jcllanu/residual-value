#Libraries
import pandas as pd

# Leer Excel
def read_excel(file):
    df = pd.read_excel(file)
    return df

def read_csv(file):
    df = pd.read_csv(file, sep=';')
    return df
def join_df ():
    full_df = pd.DataFrame()
    for i in range(30):
        file = f'Raw_Data/raw_data_{i}_OV.csv'
        df_chunks = read_csv(file)
        full_df = pd.concat([full_df,df_chunks], ignore_index= True)
        i=i+1
    full_df.to_csv(f'raw_data_OV.csv',sep=';', index=False)
    return full_df
    
# MAIN
if __name__ == "__main__":
    #full_df = join_df()
    full_df = read_csv('raw_data_OV.csv')
    print(full_df.head(5))
    num_columns = full_df.shape[1]
    print(f'number of columns {num_columns}')
    print(full_df.columns)
    missing_values = full_df['Original Value'].isnull().sum()
    total_values = full_df.shape[0]
    missing_percentage = missing_values/total_values
    print(f"Missing values in Original Value column: {missing_values}")
    print(f"Missing values: {missing_percentage}")
    
    total_por_grupo = full_df.groupby(['year_manufacture', 'make']).size().reset_index(name='total_registros')
    
    nulos_OV_por_grupo = full_df[full_df['Original Value'].isnull()] \
    .groupby(['year_manufacture', 'make']) \
    .size() \
    .reset_index(name='original_value_nulos')
        
  
    resultado_OV = pd.merge(total_por_grupo, nulos_OV_por_grupo, on=['year_manufacture', 'make'], how='left')
    resultado_OV['original_value_nulos'] = resultado_OV['original_value_nulos'].fillna(0).astype(int)

    
    resultado_OV = resultado_OV[resultado_OV['year_manufacture'] >= 2000]
    print(resultado_OV.sort_values(by='original_value_nulos', ascending=False))

    
    
    
    #nulos_por_grupo = full_df.groupby(['year_manufacture', 'make']).apply(lambda g: g.isna().sum().sum()).reset_index(name='celdas_vacias')
    #resultado = pd.merge(total_por_grupo, nulos_por_grupo, on=['year_manufacture', 'make'])
    #resultado = resultado[resultado['year_manufacture']>=2000] 
    #print(resultado.sort_values(by='celdas_vacias', ascending=False))

    #PARA CONVERTIR A NUMERO EL VALOR ORIGINAL
    #cleaned = amount_str.replace('$', '').replace(',', '')  # Remove $ and ,
    #converted = float(cleaned)

from sklearn.base import BaseEstimator, TransformerMixin


# All sklearn Transforms must have the `transform` and `fit` methods
class DropColumns(BaseEstimator, TransformerMixin):
    def __init__(self, columns):
        self.columns = columns

    def fit(self, X, y=None):
        return self

    def transform(self, X):
        # Primeiro realizamos a cópia do dataframe 'X' de entrada
        data = X.copy()
        # Retornamos um novo dataframe sem as colunas indesejadas
        data.head()
        print(data)
        return data.drop(labels=self.columns, axis='columns')
    
    
class PersFill(BaseEstimator, TransformerMixin):
    def __init__(self, dataf):
        self.dataf = dataf
        
    def fit(self, X, y=None):
        return self
         
    def transform(self, X):
        # Primeiro realizamos a cópia do dataframe 'X' de entrada
        
        data = X.copy()
        data.head()
        target = "PERFIL"
        cls = self.dataf[target].unique()
        for x in cls:
            for col in data.columns:
                if col != target:
                    self.dataf.loc[( (self.dataf[target]==x) & (self.dataf[col].isnull()) ),col] = self.dataf[col].loc[(self.dataf[target]==x)].mean()
        data = self.dataf.drop(columns =['PERFIL'])
        return data 

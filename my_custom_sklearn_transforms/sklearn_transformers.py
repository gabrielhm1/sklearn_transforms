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
        return data.drop(labels=self.columns, axis='columns')
    
    
class PersFill(BaseEstimator, TransformerMixin):
    def __init__(self, columns):
        self.columns = columns
        
    def fit(self, X, y=None):
        return self
         
    def transform(self, X):
        # Primeiro realizamos a cópia do dataframe 'X' de entrada
        
        data = X.copy()
        target = self.columns[0]
        cls = data[target].unique()
        for x in cls:
            for col in data.columns:
                if col != target:
                    data.loc[( (data[target]==x) & (data[col].isnull()) ),col] = data[col].loc[(data[target]==x)].mean()
        return data 

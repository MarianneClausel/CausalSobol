import numpy as np
from math import factorial
from dataclasses import dataclass

@dataclass
class SCMParams:
    alpha1: float=1.0
    alpha2: float=1.0
    alphaN3: float=1.0
    beta1: float=1.0
    beta2: float=1.0
    beta3: float=1.0
    betaNY: float=0.0
    sigma1: float=1.0      # standard deviation of X1
    sigma2: float=1.0      # standard deviation of X2
    
    def SCM2(self,size:int,seed:int=None)-> np.ndarray:
        if seed is None:
            np.random.seed()
        else:
            np.random.seed(seed)
        X1 = np.random.normal(0, 1.0, size)
        
        if seed is None:
            np.random.seed()
        else:
            np.random.seed(seed+1)
        X2 = np.random.normal(0, 1.0, size)
        
        if seed is None:
            np.random.seed()
        else:
            np.random.seed(seed+2)
        N3=np.random.normal(size=size)
        X3=self.alpha1*X1+self.alpha2*X2+self.alphaN3*N3
        return np.vstack([X1,X2,X3]).T #np.vstack([N3,X1,X2,X3]).T
      
    def model2(self,size: int, seed: int = None)->np.ndarray:
      if seed is None:
        np.random.seed()
      else:
        np.random.seed(seed)
        
      X=self.SCM2(size)
      X1=X[:,0]
      X2=X[:,1]
      X3=X[:,2]
      NY = np.random.normal(0, 1.0, size)
      return self.beta1*X1+self.beta2*X2+self.beta3*X3+self.betaNY*NY#np.vstack([NY,beta1*X1+beta2*X2+beta3*X3+betaNY*NY]).T

  
    



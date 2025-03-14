# Necessary packages
import numpy as np
from sklearn.metrics import cohen_kappa_score

#%% 
def mask_generator (p_m, x):
  """Generate mask vector.
  
  Args:
    - p_m: corruption probability
    - x: feature matrix
    
  Returns:
    - mask: binary mask matrix 
  """
  mask = np.random.binomial(1, p_m, x.shape)
  return mask

#%% 
def pretext_generator (m, x):  
  """Generate corrupted samples.
  
  Args:
    m: mask matrix
    x: feature matrix
    
  Returns:
    m_new: final mask matrix after corruption
    x_tilde: corrupted feature matrix
  """
  
  # Parameters
  no, dim = x.shape  
  # Randomly (and column-wise) shuffle data
  x_bar = np.zeros([no, dim])
  for i in range(dim):
    idx = np.random.permutation(no)
    x_bar[:, i] = x[idx, i]
    
  # Corrupt samples
  x_tilde = x * (1-m) + x_bar * m  
  # Define new mask matrix
  m_new = 1 * (x != x_tilde)

  return m_new, x_tilde

#%% 
def convert_matrix_to_vector(matrix):
  """Convert two dimensional matrix into one dimensional vector
  
  Args:
    - matrix: two dimensional matrix
    
  Returns:
    - vector: one dimensional vector
  """
  # Parameters
  no, dim = matrix.shape
  # Define output  
  vector = np.zeros([no,])
  
  # Convert matrix to vector
  for i in range(dim):
    idx = np.where(matrix[:, i] == 1)
    vector[idx] = i
    
  return vector

#%% 
def convert_vector_to_matrix(vector):
  """Convert one dimensional vector into two dimensional matrix
  
  Args:
    - vector: one dimensional vector
    
  Returns:
    - matrix: two dimensional matrix
  """
  # Parameters
  no = len(vector)
  dim = len(np.unique(vector))
  # Define output
  matrix = np.zeros([no,dim])
  
  # Convert vector to matrix
  for i in range(dim):
    idx = np.where(vector == i)
    matrix[idx, i] = 1
    
  return matrix

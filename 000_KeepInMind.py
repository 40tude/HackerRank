# Width 60 pour faciliter relecture sur téléphone

def Pandas() :
  ###########################################################
  # Pandas
  ###########################################################
  import pandas as pd
  df = pd.read_excel("titanic.xls")
  # read_csv ...
  df.shape
  df.columns
  print(df.head())
  # supprimer les col pas utiles
  df = df.drop(["NomColonne1", "NomColonne2"], axis=1)
  df.describe()
  
  # éviter d'utiliser 
  # df = df.fillna(df["colonne"].mean())
  
  df = df.dropna(axis=0)
  df.dropna(axis=0, inplace=True)

  # Nb d'occurences de chaque valeur
  NbPerVal = df["colonne"].value_counts() 
  print(NbPerVal[3])                           # Le nb de 3
  
  # Mieux vaut utiliser Seaborn mais...
  # Histogramme des occurences dans la colonne classe
  # df.plot()
  # df.plot.bar()
  # df.plot.hist(bins=...)
  # df.plot.scatter(x=..., y=...)
  df["classe"].value_counts().plot.bar()
  df["age"].hist()
  # bins = le nb de paquets à utiliser
  df["age"].plot.hist(bins=20)
  
  # Afficher les moyennes, regroupées par sexe
  # la colonne sexe devient les lignes (ordre alpha)
  # les autres colonnes restent en place
  print(df.groupby(['sex']).mean())
  # groupby retourne est un dataframe
  df_bysex = df.groupby(by=['sex']).mean()
  # l'ordre survived, female est important
  print(f"{df_bysex['survived']['female']:.2f} % des femmes ont survécu")
  
  df_SexClass = df.groupby(by=['sex', 'pclass']).mean()
  print(df_SexClass)
  # TO DO : comment accèder aux valeurs?


def Numpy() :
  ###########################################################
  # Numpy
  ###########################################################
  import numpy as np

  # Lignes - Colonnes
  # Row (ligne) major comme C++

  A.shape          # tuple avec la taille de chaque dimension
  A.ndim           # le nb de dimensions
  A.size           # le nb de cellules

  A = np.array([0, 1, 2, 3])                # 1D et 4 ele
  B = np.array([1,2,3]).reshape(3,1)        # Z! Important                     
  B = B.squeeze()                           # (3, 1) -> (3, )
  C = np.array([i for i in range(100, 109)]).reshape(3,3)
  # Dataset (dico) de 10 expériences avec 100 pts chacunes
  Dataset = {f"Experience{i}" : np.random.randn(100) for i in range(10)} 
  # 3 lignes, 4 col avec des valeurs entre 0 et 1
  # n comme normalized 
  # y a aussi un np.random.seed(0)
  D = np.random.randn(3,4)                    
                                              
  # 5x5 - [0, 100[. 
  # Voir https://numpy.org/doc/stable/reference/random/index.html#random-quick-start                                             
  D = np.random.randint(0, 100, [5,5])        

  # matrice identité 4x4
  E = np.eye(4)                               

  # 100 points entre [10 et 20]
  F = np.linspace(10, 20, 100)                

  # n points entre [10 et 20[ au pas de .7  
  G = np.arange(10, 20, .7, dtype=np.float16) 

  # passer un tuple
  Tab1 = np.zeros((3,2))                      
  Tab2 = np.ones((3,2))

  # axis = 0 => vertical
  Tab5 = np.concatenate((Tab1, Tab2), axis=0) 

  # axis = 1 => horizontal   
  Tab6 = np.concatenate((Tab1, Tab2), axis=1) 
  Tab7 = Tab6.reshape(6, 2)  

  # transforme en tableau 1D. 
  # Utile pour 
  # optimize.minimize (x0)
  # les spectres d'images 
  # les images en entrée de réseau de neurones
  Tab13 = Tab1.ravel()                     

  X = np.random.randn(3, 4)
  X[:,-1:] = 1           # met des 1 dans la dernière colonne

  # slicing A[debut:fin:pas, debut:fin:pas]
  print("Colonne 0 : ", A[:, 0])
  print("Colonne 2 : ", A[:, 2])
  print("Ligne 1   : ", A[1, :])
  print("Ligne 2   : ", A[2])                    

  # subseting. /!\ de 0 à 2 exclu
  B = A[0:2, 0:2]                              

  # Initialise une sous-partie de la matrice
  A[0:2, 0:2] = 100                         

  # copier les 2 dernières colonnes
  D = C[:,-2:]                              

  # remplir en damier  
  E[::2, ::2] = 1                          

  # mettre à 100 selon condition
  A[(A<5) & (A>2)] = 100                    

  # Filtrage
  A = np.random.randint(0, 10, [5,5])
  # A n'est plus une matrice mais un vecteur!
  A[A<5]                                    

  A = np.random.randint(0, 10, [5,5])    
  # normalized, entre 0 et 1    
  B = np.random.randn(5, 5)                 
  # C est un vect. Contient les valeurs de B qui passent le 
  # filtre appliqué à A
  C = B[A<2]                                

  # somme de tous les éléments
  A.sum()                                   

  # un vecteur de col éléments. Somme selon chaque colonne
  A.sum(axis=0)                             
  # un vecteur de A.size élé
  # contient la somme cumulée en row major (ligne à ligne)
  A.cumsum()                                
  # Une matrice. 
  # Sur chaque ligne, somme cumulée le long des colonnes
  A.cumsum(axis=1)                          
  # un vecteur avec la position des minimums dans les colonnes
  A.argmin(axis=0)                          
  # une matrice de même dimension que A. Contient les indices
  # pour trier sur chaque ligne, selon les colonnes 
  A.argsort(axis=1)                         
  A.mean()
  # moyenne des colonnes
  A.mean(axis=0)                            
  A = np.exp(A)

  # Matrice des coefs de correlation entre les lignes de A
  np.corrcoef(A)                            
  # Coef de correlation entre les lignes 0 et 1 de A
  np.corrcoef(A)[0,1]                       

  # retroune les valeurs classées et leurs nombres d'apparations
  V, C = np.unique(A, return_counts=True)   
  # Les index des occurences pour les trier en ordre croissant
  B = C.argsort()                           
  # Les valeurs triées par nombre d'occurence croissant 
  V[C.argsort()]                            

  # V = values, C = Counts
  for i,j in zip(V[C.argsort()], C[C.argsort()]): 
    # zip agrège des itérables dans un tuple
    print(f"La valeur {i} apparaît {j} fois.")    

  # met un Nan dans en 4,3 dans matrice A
  A[4,3]= np.nan                            
  # moy avec des Nan dans la matrice
  np.nanmean(A)                             

  # masque booléen avec T quand y a un Nan
  B = np.isnan(A)                           
  # compter les Nan
  NbDeNan = B.sum()                         
  Qualité = NbDeNan/A.size

  # # On remplace les Nan par 0.0
  A[np.isnan(A)]=0.0                        

  # Algèbre linéaire
  # Transposée
  A.T                                       
  A.dot(B)
  # déterminant
  np.linalg.det(A)                          
  # inverse
  np.linalg.inv(A)                          
  # valeurs propres
  np.linalg.eig(A)                          

  # Broadcasting
  # Etendre les dimensions d'un tableau
  # REGLE : 
  # les dimensions de A et B doivent être identiques
  # ou alors l'une des 2 est égale à 1
  # Matrice (2,3) et matrice (2,3) OK
  # Matrice (2,3) et matrice (2,2) NOK
  # Matrice (2,3) et matrice (2,1) OK (on transforme le 1 en
  # 3. On répette à droite le motif (2,1) pour couvrir (2,3))
  # Matrice (2,3) et matrice (3,1) NOK
  # Matrice (4,1) et matrice (1,3) OK (on broadcast dans les 
  # 2 axes)

  # ajoute 2 partout. scalaire == tableau 1x1
  A = A + 2                                 
  # A et B même shape
  C = A + B                                 

  A = np.random.randint(0,100,(2,3))
  B = np.ones((2,1))                        
  # B est étendue et dupliquée à droite 2 fois (3 colonnes)  
  # l'addition se fait ensuite
  A+B                                       
                                            

  A = np.random.randint(0,100,(2,3))
  B = np.ones((1,3))
  # B est étendue et dupliquée en bas 2 fois (3 lignes)
  # l'addition se fait ensuite
  A+B                                       
                                            

  A = np.random.randint(0,100,(4,3))
  B = np.ones((1,3))
  A+B

  A = np.random.randint(0,100,(4,1))
  B = np.ones((1,3))
  # Matrice 4x3. 
  # A est étendue en bas 2 fois (3 lignes) et le contenu de 
  # la ligne est répété
  # B est étendue à droite 3 fois (4 colonnes) et le contenu
  # de la colonne est répété
  # l'addition se fait ensuite
  A+B                 

  # Z! broadcast intenpestifs. Utiliser reshape
  A = np.random.randint(0,10,(4,1))
  B = np.ones((3))
  B = B.reshape(3,1)


def Matplotlib() :
  ###########################################################
  # Matplotlib
  ###########################################################
  import matplotlib.pyplot as plt

  # Explicit - OO ###########################################
  import numpy as np
  import matplotlib.pyplot as plt
  x = np.linspace(0, 2, 100)
  y = x**2
  fig, ax = plt.subplots()      
  ax.plot(x, y)


  import numpy as np
  import matplotlib.pyplot as plt
  x = np.linspace(0, 2, 100)
  y = x**2
  fig, axs = plt.subplots(2, 1, sharex=True) 
  axs[0].plot(x, y)
  axs[0].set_ylim([None, 8]) 
  axs[1].plot(x, x**3, c="red", lw=5, ls="--")

  import numpy as np
  import matplotlib.pyplot as plt
  x = np.linspace(0, 2, 10)
  y = x**2
  fig, ax = plt.subplots()        # bien voir le s à subplots
  ax.plot(x, y, label="Camion", c="red")
  ax.scatter(x, x**3, label="vehicle 1")
  fig.suptitle ("Figure")
  ax.set_title("Axe")
  ax.set_xlabel("Time (s)")
  ax.set_ylabel("Speed (m/s)")
  ax.legend() 
  fig.savefig("Figure.png")
    

  # Implicit - Classic ######################################
  import numpy as np
  import matplotlib.pyplot as plt
  x = np.linspace(0, 2, 100)
  y = x**2
  plt.plot(x, y)  
  plt.show()       

  import numpy as np
  import matplotlib.pyplot as plt
  x = np.linspace(0, 2, 100)
  y = x**2
  plt.subplot(2, 1, 1)              
  plt.plot(x, y, c="red")
  axes = plt.gca()                         # Get current axes
  axes.set_ylim([None, 8])
  plt.subplot(2, 1, 2)              
  plt.plot(x, x**3, c="blue")
  plt.show()


  ###########################################################
  fig, axs = plt.subplots(n//2, n//2, figsize=(12, 12/1.618)) 
  # here axs is a matrice not a 1D array
  axs = axs.ravel()
  for i, ax in enumerate(axs) :
    ax.scatter(x[:, 0], x[:, i], c = y)
    ax.set_xlabel("0")
    ax.set_ylabel(i)
  plt.show() 

  # trace x1 en fonction de x0. Couleur en fonction de y. 
  # Taille en fonction de x2
  ax.scatter(x[:, 0], x[:, 1], c=y, alpha=0.5, s=x[:,2]*100)        

  # 3D scatter
  fig, ax = plt.subplots(subplot_kw={'projection': '3d'})
  ax.scatter(x, y, z, c=y, alpha=0.5)

  # 3D surface
  f=lambda x, y : np.sin(x) + np.sin(x+y) 
  x=np.linspace(0, 5, 10)  
  y=np.linspace(0, 5, 10)
  # x vec lign étend en bas, y vec col étend à dte       
  x, y = np.meshgrid(x, y) 
  z = f(x,y)
  fig, ax = plt.subplots(subplot_kw={'projection': '3d'})
  ax.plot_surface(x, y, z, cmap="plasma")  
  # cmap https://matplotlib.org/stable/tutorials/colors/colormaps.html

  # Histogramme
  fig, axs = plt.subplots(2, 1)
  axs[0].hist(x[:,0])
  # bins = le nb de paquets à utiliser
  axs[0].hist(x[:,0], bins=20)
  axs[0].set_title("2 fois le même jeu mais nb de bins différents")
  axs[1].hist(x[:,0])
  axs[1].hist(x[:,1])
  axs[1].set_title("2 jeux différents")

  # Hist 2D - Pas un mapcolor
  # Suivre la distribution des données 
  # quand elles suivent 2 variables
  fig, ax = plt.subplots()
  h = ax.hist2d(x[:,0], x[:,1])
  ax.set_xlabel("Info 1")
  ax.set_ylabel("Info 2")
  cbar = fig.colorbar(h[3]) # ,ax=ax
  plt.show()

  # Hist image N&B
  face = misc.face(gray=True)
  plt.imshow(face, cmap="gray")
  fig, ax = plt.subplots()
  # bins = le nb de paquets à utiliser
  ax.hist(face.ravel(), bins=255)
  plt.show() 

  # Contour plot
  Cs1 = ax.contour(x, y, z, 10, colors="red")
  Cs2 = ax.contourf(x, y, z, 10, cmap=cm.jet)
  ax.clabel(Cs1, inline=1, fontsize=8, colors="black")
  cbar = fig.colorbar(Cs2)
  cbar.add_lines(Cs1)

  # Image
  fig, ax = plt.subplots()
  im = ax.imshow(np.corrcoef(x.T), cmap=cm.jet)
  fig.colorbar(im)
  plt.show()


def Scipy() :
  ###########################################################
  # Scipy
  ###########################################################
  # Interpolate
  from scipy.interpolate import interp1d
  x = np.linspace(0, 10, 10)
  y = x**2
  f = interp1d(x, y, kind='linear')
  x2 = np.linspace(0, 10, 100)        # 10 fois plus de points
  ax.scatter(x2, f(x2), s=1, c='red')

  # Optimize
  from scipy import optimize
  def MyF (x, a, b, c, d):
    return a * x**3 + b*x**2 + c*x +d

  # Voir plutôt SkitLearn
  Param, MatParamCov = optimize.curve_fit(MyF, x, y)
  ax.plot(x, MyF(x, Param[0], Param[1], Param[2],Param[3]), c="green", lw="2")


  # Minimize
  def f(x):
    return x**2 + 15*np.sin(x)

  x0=-7.5
  Info = optimize.minimize(f, x0) 
  xmin = Info.x
    
  # Minimize2D
  def f3(pt):
    return np.sin(pt[0]) + np.cos(pt[0]+pt[1])*np.cos(pt[0])

  Pt0 = np.zeros((2,))                # /!\ c'est bien (2, )
  Info = optimize.minimize(f3, Pt0) 
  PtMin = Info.x

  # Eliminer la tendance linéraire du signal
  from scipy import signal
  y1 = signal.detrend(y)

  # FFT
  from scipy import fftpack

  tft = fftpack.fft(y)
  freq = fftpack.fftfreq(y.size)
  ax.plot(np.abs(freq), np.abs(tft)) # /!\ abs

  # filtre les valeurs de la TFT 
  power = abs(tft)
  tft[power<seuil] = 0.0
  axs.plot(np.abs(freq), np.abs(tft))

  # fft inverse
  Filtered = fftpack.ifft(tft)
  axs.plot(x, Filtered)

  # images
  from scipy import ndimage

  image = plt.imread("Bacteria.png")
  # penser à vérifier dimensions
  print(image.shape)
  #subseting, enlève la 3eme dimension
  image = image[:,:,0] 

  # affichage
  fig, ax = plt.subplots()
  ax.imshow(image)

  # histogramme
  image = np.copy(image)
  fig, ax = plt.subplots()
  # bins = le nb de paquets à utiliser
  ax.hist(image.ravel(), bins=255)

  # Masque de booléens qu'on peut utiliser 
  # comme une image binaire
  image  = image < 0.6

  # retirer les pixels isolés
  open_x = ndimage.binary_opening(image)

  # labeliser le contenu
  LabeledImage, NbLabels = ndimage.label(open_x)

  # Compter afficher le nb de pixels dans chaque bactérie
  sizes = ndimage.sum_labels(open_x, LabeledImage, range(NbLabels))
  fig, ax = plt.subplots()
  ax.scatter(range(NbLabels), sizes)  


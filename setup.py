from setuptools import setup, find_packages

setup(name='yolact',
      version='1.0.0',
      description='Pytorch Library of yolact for Instance Segmentation',
      author='Federico Rollo',
      author_email='rollo.f96@gmail.com',
      url='https://github.com/robolableonardo/yolact',
      install_requires=[
          'numpy', 'torch>=1.4.0', 'torchvision>=0.5.0', 'Pillow', 'scipy',
          'scikit-learn', 'metric-learn', 'cython', 'opencv-python',
          'pycocotools', 'matplotlib'],
      packages=find_packages(),
      keywords=[
          'Instance Segmentation',
          'Deep Learning',
      ])

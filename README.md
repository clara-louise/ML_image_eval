# ML_image_eval
Ada coursework - Evaluation script for image classification

Current version is designed to work with two classes only.

1. Download your model from Teachable Machine in Tensoflow Keras format.
2. Replace the contents of the "converted keras" folder with your model and the contents of the "test_data" with your data.
3. Run eval.py. to print the predictions of your model and scores to the command line.

example output: <br/>

Dingo test images, predicted class and score<br/>
n02115641_8798.jpg, Dingo, 0.99648017<br/>
n02115641_8871.jpg, Dingo, 0.997614<br/>
n02115641_8682.jpg, Dingo, 0.9999658<br/>
n02115641_8578.jpg, Dingo, 0.9531685<br/>
n02115641_8746.jpg, Dingo, 0.9930635<br/>

Cardigan test images, predicted class and score<br/>
n02113186_10077.jpg, Cardigan, 0.9992785<br/>
n02113186_10416.jpg, Cardigan, 0.99997723<br/>
n02113186_10361.jpg, Cardigan, 0.9944348<br/>
n02113186_10431.jpg, Cardigan, 0.9998894<br/>
n02113186_9935.jpg, Cardigan, 0.9999114<br/>

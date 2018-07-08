# 线性拉伸对比度的例子
# http://scikit-image.org/docs/dev/user_guide/transforming_image_data.html#contrast-and-exposure
#
# Jianjiang Feng
# 2018.7.8

from skimage import data
from skimage import exposure
import matplotlib.pyplot as plt
import numpy as np

I = data.text()
#I = data.moon() # moon的极值是0和255
print('I: Min %d, Max %d' % (I.min(), I.max()))

I2 = exposure.rescale_intensity(I)
print('I2: Min %d, Max %d' % (I2.min(), I2.max()))

v_min, v_max = np.percentile(I, (0.2, 99.8))
print('I: PMin %d, PMax %d' % (v_min, v_max))

I3 = exposure.rescale_intensity(I, in_range=(v_min, v_max))
print('I3: Min %d, Max %d' % (I3.min(), I3.max()))

plt.figure(1)
plt.subplot(1,3,1)
plt.imshow(I, cmap='gray')
plt.subplot(1,3,2)
plt.imshow(I2, cmap='gray')
plt.subplot(1,3,3)
plt.imshow(I3, cmap='gray')
plt.show()
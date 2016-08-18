# ImageGenerator
:heartpulse: 一款比较实用的小工具，根据给定像素的标准图片，生成适配不同屏幕的套图。尤其适用于Android开发

如果您觉得还不错，给我点个星星吧 :heartpulse:
---

使用Python做起工具来还真是爽，简单，方便，快捷。今天忙活了一下，制作出一个比较实用的小工具。

[自动化套图制作，适配不同屏幕](https://github.com/guoruibiao/ImageGenerator)

尤其是对于android开发来说，要适配不同屏幕就需要多套切图，那么。这款工具将让你脱离切图的苦海，拥抱愉快开发的怀抱。
![自动化屏幕适配](http://img.blog.csdn.net/20160818214816490)

---

## 编程之禅
 
 这次的工具制作，可谓是煞费苦心了。我尝试着让自己处于一个用户的角度，来思考整个流程的实现，最终得到了一个比较不错的结论。

<font color="green" size="5">less operations, more goods</font>

所以，基本上来说，我隐藏了底层实现的很多的细节。

## 怎么使用？

这个工具使用起来也是相当的简单的。如下：

因为这个工具是基于Python2.7开发的，所以需要有Python环境的支持。

- 第一步：任意找到一个文件夹

> python ImageGenerate.py init 

来执行初始化工作目录的工作，执行结束后，我们会发现当前文件夹下多了几个目录。下面详细介绍一下：

- 第二步：在modules目录下的cfg.txt文件中写上如下类型的数据：

```
1080x1920
1128x1920
423x800
480x800
552x1024
600x1024
720x1024
736x1280
752x1280

```
再次执行
> python ImageGenerate.py init 

就可以看到下面的文件结构：

```
E:\Code\Python\DataStructor\release>tree
卷 文档 的文件夹 PATH 列表
卷序列号为 0000-4823
E:.
├─destination     用于存放生成的不同的屏幕适配图片
│  ├─1080x1920
│  ├─1128x1920
│  ├─423x800
│  ├─480x800
│  ├─552x1024
│  ├─600x1024
│  ├─720x1024
│  ├─736x1280
│  └─752x1280
├─modules           存放配置文件，也即是分辨率方案，待会详谈
└─source            标准的美工图片1080*1920分辨率即可，将作为我们的图片生成参考

```


- 第三步，批量生成：在source文件夹下面放置要生成套图的标准图片即可，任意张数

> python ImageGenerate.py generate

 该命令的工作原理是，根据source文件夹下列出的标准图片，来生成不同分辨率的匹配图，且给予良好的命名规范，便于用户使用。

结果如下：

```
E:.
│  ImageGenerate.py
│
├─destination
│  ├─1080x1920
│  │      beauty-1080x1920.png
│  │      resize-1080x1920.png
│  │
│  ├─1128x1920
│  │      beauty-1128x1920.png
│  │      resize-1128x1920.png
│  │
│  ├─423x800
│  │      beauty-423x800.png
│  │      resize-423x800.png
│  │
│  ├─480x800
│  │      beauty-480x800.png
│  │      resize-480x800.png
│  │
│  ├─552x1024
│  │      beauty-552x1024.png
│  │      resize-552x1024.png
│  │
│  ├─600x1024
│  │      beauty-600x1024.png
│  │      resize-600x1024.png
│  │
│  ├─720x1024
│  │      beauty-720x1024.png
│  │      resize-720x1024.png
│  │
│  ├─736x1280
│  │      beauty-736x1280.png
│  │      resize-736x1280.png
│  │
│  └─752x1280
│          beauty-752x1280.png
│          resize-752x1280.png
│
├─modules
│      cfg.txt
│
└─source
        beauty.png
        resize.png

```


## 拓展
为了支持更多的屏幕适配方案，本工具特地使用了配置文件来维护，也就是modules/cfg.txt文件。 

注意：

<font color='green' size='5'> 以字典顺序书写width*height格式</font>，如：

```

1080x1920
1128x1920
423x800
480x800
552x1024
600x1024
720x1024
736x1280
752x1280
```

好了，就是这样了。源码也已经上传到GitHub，如果你对这个小工具也很感兴趣，可以和我取得联系。

:-)

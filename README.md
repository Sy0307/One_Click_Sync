# One_Click_Sync

一键同步文件到本地的多个仓库 One-click synchronization of files to multiple local repositories

图源[[まごつき](https://www.pixiv.net/users/5472279)]

![image.png](https://s2.loli.net/2023/02/24/gTis4vHydmQMb86.png)

## 作用

同步一份文件夹下的所有文件，通过本仓库，你可以将其更新到其他目录下。（每次都手动移动太麻烦了吧！）

## 使用方法

我们把经常使用，需要同步到其他路径的文件夹叫做`SOURCE_DIR`源文件夹。

而其他做备份使用的仓库我们称之为`TARGET_DIRS`，目标文件夹。

首先，你需要：

- 将`SOURCE_DIR`改为你需要同步的本地路径。
- 或者不修改`Sync.py`，将`Sync.py`以及`run.bat`移动到你需要备份的目录下。

其次，将`TARGET_DIRS`使用Append方法，添加你需要同步备份的本地路径。

然后你点击`run.bat`即可！

（当然仅仅使用于`Windows`）

### 额外功能

- 过滤文件：向`Sync.py`中的`FILTER_FILE_NAME`添加你需要过滤的文件名即可！


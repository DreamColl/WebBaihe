# baihe_web

####1.将npm转为cnpm（淘宝镜像库，节省安装等待时间）
    npm install -g cnpm --registry=https://registry.npm.taobao.org

####2.输入以下指令
    cnpm i 安装node_modules
    npm run build 生产环境
    dist的文件夹内会生成所有线上需要使用的东西

####3.[完整的npm指令教程](http://javascript.ruanyifeng.com/nodejs/npm.html)
    常用的指令
    cnpm insatll XXX -D(--save-dev) 安装devDependencies 开发环境包（通常在此处安装）
    cnpm insatll XXX -S(--save) 安装Dependencies 生产环境包（少数环境包）

####4.坑
    config/index.js 
    第10行 '/'改为'./'
    第11行 改为false 不生成map
<!-- 
以下是命名结构方法:
五段式结构：
SRC – [波段][距离级][结构] – [第几代][用途]

第一段（固定前缀）
SRC = Surveillance Radar by Cyrentis

第二段：波段
代码	波段
C	C band
X	X band
K	Ku band

第三段：探测等级
直接用数字，不要写 km。
等级	典型无人机探测
01	1.5 km
03	3 km
05	5 km
08	8 km
10	10 km
20	20 km
50	50 km

第四段：Scanning Architecture Classification

The scanning architecture code defines the radar beam steering configuration and coverage method.
To simplify product identification while maintaining technical clarity, the scanning modes are categorized into five types (A–E).

Code	Scanning Architecture	Description
A	Azimuth Electronic Scanning	Fixed-array radar with electronic beam steering in the horizontal (azimuth) direction.
B	Mechanical Azimuth Scan + Electronic Elevation Scan	Mechanically rotating antenna providing 360° azimuth coverage with electronic beam steering in elevation. This configuration is commonly used in rotating surveillance radars.
C	Two-Dimensional Electronic Scanning (Single-Face AESA)	Single-face active electronically scanned array providing electronic beam steering in both azimuth and elevation within a sector coverage.
D	2D Electronic Scanning + Mechanical Rotation	Active electronically scanned array mounted on a rotating platform, combining electronic beam steering with mechanical rotation for wide-area coverage.
E	Four-Face AESA (Full Electronic Coverage)	Radar employing four fixed AESA panels to achieve continuous 360° coverage through electronic scanning without mechanical rotation.

第五段:第几代
在暂时目前表示的是体制
代码	体制
1	FMCW 调频连续波
2	Pulse Doppler 脉冲多普勒
3	Pulse Doppler 脉冲多普勒


第六段:用途
最后一个字母表示用途：
代码	用途
D	Drone detection
G	Ground surveillance
M	Multi-purpose

按照这个命名法添加下列产品,每个产品都需要有单独的详情页, 按照名称和后面的要求来自由发挥一些参数, 
所有雷达都在complete-products/radar/这个list页面用卡片的形式展现, 每个卡片包含缩略图, 型号(完整字符串), 波段(字母), 最大探测距离(数字加km),体制(FMCW 或者脉冲多普勒),结构(五种结构的简要解释). 用途(用svg或者公共库里分别取行人1,车辆2,船只3,无人机4 一共四种目标的图标, 如果类型为D, 则显示4, 如果类型为G则显示1,2,3. 如果为M则显示全部4个) ,并根据下面提示的亮点显示一条highlight图标和文本.
以下信息的格式为: 型号名称 (探测目标和距离)[亮点功能][量程]
SRC-C08A-1G (人:2km,车:5km, 船8km)[亮点:入门体验][量程10km]
SRC-X01C-1D (小无人机1.5km)[亮点:近距离单面防御][量程3km]
SRC-X01D-1D (小无人机1.5km)[亮点:近距离全方位防御][量程3km]
SRC-X01E-1D (小无人机1.5km)[亮点:可靠性][量程3km]
SRC-X03C-1D (小无人机3km)[亮点:精准单面防御][量程5km]
SRC-X03D-1D (小无人机3km)[亮点:中距离全方位防御][量程5km]
SRC-X03E-1D (小无人机3km)[亮点:可靠性][量程5km]
SRC-X05C-1D (小无人机5km)[亮点:精准单面防御][量程10km]
SRC-X05D-1D (小无人机5km)[亮点:多数客户选择][量程10km]
SRC-X05E-1D (小无人机5km)[亮点:可靠性][量程10km]
SRC-K05C-1D (小无人机5km)[亮点:精准单面防御][量程10km]
SRC-K05D-1D (小无人机5km)[亮点:多数客户选择][量程10km]
SRC-K05E-1D (小无人机5km)[亮点:可靠性][量程10km]
SRC-X10C-1D (小无人机10km)[亮点:精准单面防御][量程15km]
SRC-X10D-1D (小无人机10km)[亮点:多数客户选择][量程15km]
SRC-X10E-1D (小无人机10km)[亮点:可靠性][量程15km]
SRC-K01B-2D (小无人机1.5km)[亮点:近距离单面防御][量程3km]
SRC-K03B-2D (小无人机3km)[亮点:中距离单面防御][量程5km]
SRC-X05B-2D (小无人机5km)[亮点:中距离单面防御][量程10km]
SRC-X08B-2D (小无人机8km)[亮点:远距离单面防御][量程20km]
SRC-X10B-2D (小无人机10km)[亮点:远距离单面防御][量程20km]
SRC-X05E-3D (小无人机5km)[亮点:可靠性][量程10km]
SRC-X08E-3D (小无人机8km)[亮点:可靠性][量程10km]
SRC-K05E-2G (人2km,车5km)[亮点:中距离单面防御][量程10km]
SRC-K10A-2G (人4km,车6km,船10km)[亮点:远距离单面防御][量程15km]
SRC-X12A-2G (人5km,车8km,船12km)[亮点:远距离单面防御][量程20km]
SRC-X25A-2G (人10km,车16km,船25km)[亮点:远距离单面防御][量程30km]
SRC-X50A-2G (人16km,车28km,船50km)[亮点:覆盖距离最远][量程50km]

每个雷达详情页的信息包括:
1. 标题和简介,以及所有SEO可能会用到的信息,根据情况来添加,确保格式统一, 将一些参数写在frontmatter方便后续修改和在list页面添加filter.
2. 每个雷达使用一张图片,图片用雷达名称后面括号里的image路径获取,用做详情页的主图和,list页的缩略图. 图片原始大小为600x400(目前的图片大小不一后期会统一成600x400).
3. 在标题附近的前面位置标识出雷达的特征参数,主要是波段(C,X, KU), 结构(ABCDE的简要解释), 每个所支持的目标对于对应的距离,距离用横向bar来表示,最长长度为设备的量程.
4. 在波段的后面添加Tips图标(优先svg)和文字, 在information的knowledge base下新建一篇图文并茂的文章来说明各种不同的波段的pro和con以及如何根据场景和目标来选择适合的频段的文章. 并链接到此处.
5. 在结构的后面添加Tips图标(优先svg)和文字, 在information的knowledge base下新建一篇图文并茂的文章来说明5种不同结构的优缺点和技术路线,着重强调其适合不同的环境. 并链接到此处.
6. 技术参数主要包含:波段,探测范围,模式(这三个已经多次出现,和前面保持一致), 盲区, 水平视场角,俯仰视场角,测速范围,转台转速(只有B和D有转台,其他的此参数写N/A),数据更新率,同时跟踪目标数(分TWS和TAS), 距离精度,方位角精度,俯仰角精度(A类型产品不可用),通讯接口,供电范围,功耗,环境适应性,重量,尺寸.
7. 添加一些常见的FAQ. 涵盖一下方面的知识:
    a. 我们是经销商不是厂家,我们展示雷达产品由国内专业的雷达厂家制造, 他们专注于制造, 你从我们这里能获得更多的支持和配合以及渠道价格的优惠.
    b. 我们的雷达提供通讯协议,客户可以很方便地进行与其他系统比如光电产品,软杀伤硬杀伤控制进行集成,我们也可以提供一体化集成服务.
    c. 雷达的使用很方便,任何工厂在阅读说明书后可以很快速的进行拆装和部署. 机动性非常强.
    d. 我们的雷达使用AI训练模型,在目标识别的准确率上有了大幅度的提升,在马来西亚等雨林多鸟的环境下也经过了测试.
    e. 我们的产品仅限安防民事用途,雷达属于中华人民共和国的出口管制物品,需要办理合规的两用物项许可证. 在knowledge base下面再新建一篇文章说明两用物项相关的官方要求.

在listy添加filter和一些说明让用户可以根据下列参数来过滤将要展示的所有雷达card:
1. target类型, 4个图标的checkbox,附带分别的参考RCS面积. 默认为空
2. 距离,用户选择

修改list页面的卡片显示:
1. 移除 read more 按钮, 改为鼠标hover整个card的区域时候, 缩略图出现轻微放大效果(保持可视区域尺寸不变),并且边框出现高亮显示效果,点击卡片的图片和型号文本区域都可进入详情页.
2. 移除Max detection range
3. System type 两端对齐
4. 将highlight的中文翻译成英文并替换成合适的英文badge
5. 将Purpose行删除, 改为"Detection Range", 然后再下方用对应的图标和bar来显示距离, 例如行人就用表示行人图标(建议50x50左右的深色图标避免太小看不清,可以从公共库下载后放在本地引用),后面用bar来表示, bar的高亮长度和总长度的占比使用 targets里对应的距离和max_range_km的比例, 例如max_range_km为3,而target是1.5, 则显示一个长度占据后续div宽度大概1半的蓝色bar, 然后在右侧显示文本1.5km



主要产品结构:
1. 低空探测 - 雷达(宝威和讯尔),光电(便携,固定式[合普]),频谱(便携,固定式),干扰(便携式,固定式).
2. 探测组件中心 -  电源, PA, LNA, 特定频率的干扰,光电组件.
3. 
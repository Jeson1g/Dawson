import re

# 正则表达式的分组
ret = re.match(r"<(?P<regex1>\w*)>\w*</(?P=regex1)>", "<html>books</html>")

print(ret.group())

# search只匹配一个
ret = re.search(r"\d+", "阅读次数为 9999")

# findall匹配全文，返回的是一个列表
ret1 = re.findall(r"\d+", "python = 9999, c = 7890, c++ = 12345")

# sub将匹配到的数据进行替换，第二个参数还可以接收一个函数对象
ret2 = re.sub(r"\d+", '998', "python = 997")

string = """<div>
        <p>岗位职责：</p>
<p>完成推荐算法、数据统计、接口、后台等服务器端相关工作</p>
<p><br></p>
<p>必备要求：</p>
<p>良好的自我驱动力和职业素养，工作积极主动、结果导向</p>
<p>&nbsp;<br></p>
<p>技术要求：</p>
<p>1、一年以上 Python 开发经验，掌握面向对象分析和设计，了解设计模式</p>
<p>2、掌握HTTP协议，熟悉MVC、MVVM等概念以及相关WEB开发框架</p>
<p>3、掌握关系数据库开发设计，掌握 SQL，熟练使用 MySQL/PostgreSQL 中的一种<br></p>
<p>4、掌握NoSQL、MQ，熟练使用对应技术解决方案</p>
<p>5、熟悉 Javascript/CSS/HTML5，JQuery、React、Vue.js</p>
<p>&nbsp;<br></p>
<p>加分项：</p>
<p>大数据，数理统计，机器学习，sklearn，高性能，大并发。</p>

        </div>"""
if __name__ == '__main__':
    ret = re.sub(r"<[^>]*>|&nbsp;|\n", "", string)

    print(ret)


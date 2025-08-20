import streamlit as st
from PIL import Image

# 设置页面
st.set_page_config(
    page_title="澄漪生态，云水潘安 - 潘安湖生态保护",
    page_icon="🌿",
    layout="wide",
    initial_sidebar_state="expanded"
)

# 加载CSS样式
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

local_css("utils/style.css")

# 标题和介绍
col1, col2 = st.columns([1, 3])
with col1:
    st.image("images/header.jpg", width=150)
with col2:
    st.title("澄漪生态，云水潘安")
    st.subheader("潘安湖生态保护社会实践团")

st.markdown("---")

# 引言部分
st.header("引言：从理念到实践，探寻绿色发展之路")
st.markdown("""
“绿水青山就是金山银山”这一科学论断，不仅是中国生态文明建设的核心理念，更是实现人与自然和谐共生的重要指引。
在江苏徐州的潘安湖畔和马庄村，这一理念被赋予了鲜活的生命力。通过生态修复和乡村振兴的双重实践，
这里成为了全国范围内践行"两山理论"的典范。
""")

# 使用两列布局展示两个地点的概览
col1, col2 = st.columns(2)

with col1:
    st.subheader("🌊 潘安湖生态修复")
    st.image("images/lake1.jpg", use_column_width=True)
    st.markdown("""
    - 从煤矿塌陷区到国家湿地公园的华丽蜕变
    - 植被覆盖率大幅提升，栖息200多种鸟类
    - 生态旅游带动区域经济发展
    """)
    if st.button("了解更多潘安湖信息 →", key="lake_btn"):
        st.switch_page("pages/1_潘安湖生态.py")

with col2:
    st.subheader("🏡 马庄村乡村振兴")
    st.image("images/village1.jpg", use_column_width=True)
    st.markdown("""
    - 从矿区村庄到全国文明村的转型之路
    - 特色香包产业带动文化传承与经济发展
    - 党建引领下的美丽乡村建设典范
    """)
    if st.button("了解更多马庄村信息 →", key="village_btn"):
        st.switch_page("pages/2_马庄村振兴.py")

st.markdown("---")

# 启示部分
st.header("实践启示")
st.markdown("""
通过对潘安湖生态修复和马庄村乡村振兴的实地调研，我们总结出以下重要启示：
""")

tab1, tab2, tab3 = st.tabs(["理念先行", "多方协同", "创新驱动"])

with tab1:
    st.subheader("理念先行：坚持'两山理论'不动摇")
    st.markdown("""
    无论是潘安湖的生态修复还是马庄村的乡村振兴，其成功都离不开对"绿水青山就是金山银山"理念的深刻理解和坚定执行。
    这提醒我们，发展理念决定发展方向，唯有尊重自然规律，才能找到可持续发展的正确道路。
    """)

with tab2:
    st.subheader("多方协同：政府、市场与社会共同发力")
    st.markdown("""
    潘安湖的生态修复离不开政府的政策支持和技术投入，马庄村的文化振兴则得益于市场的敏锐嗅觉和社会的广泛参与。
    这说明，单靠某一方的力量难以奏效，必须构建多元主体协同合作的机制。
    """)

with tab3:
    st.subheader("创新驱动：因地制宜探索特色路径")
    st.markdown("""
    每个地区都有独特的资源禀赋和发展条件，关键在于如何发现并利用这些优势。
    潘安湖和马庄村的经验告诉我们，只有立足本地实际，勇于创新，才能开辟属于自己的发展道路。
    """)

st.markdown("---")

# 结语
st.header("结语")
st.markdown("""
潘安湖的碧波荡漾与马庄村的田园风光，共同讲述了一个关于希望与奋斗的故事。它们用事实证明，
"绿水青山就是金山银山"不是一句空洞的口号，而是可以落地生根、开花结果的伟大实践。

**愿每一片绿水青山，都能成为造福人民的金山银山！**
""")

# 页脚
st.markdown("---")
footer_col1, footer_col2, footer_col3 = st.columns(3)
with footer_col2:
    st.markdown(
        '<div style="text-align: center; color: gray;">潘安湖生态保护社会实践团 © 2023</div>',
        unsafe_allow_html=True
    )
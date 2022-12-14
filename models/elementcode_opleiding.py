class ElementcodeOpleiding:
    ELEMENTCODES = {
        "0802": "ESS 1-5",
        "0803": "ESS 6-7",
        "0700": "IB middle years programme",
        "0800": "IB diploma programme",
        "0801": "IB diploma programme Dutch res",
        "0804": "IB career-related programme",
        "0805": "IB career-rel. prog. Dutch res",
        "0090": "praktijkonderwijs",
        "0024": "vmbo/havo/vwo voorbereid. Lj",
        "0016": "vmbo-gl/tl/havo/vwo voorb. lj",
        "0017": "vwo voorbereid. lj",
        "0200": "vwo-gymnasium onderbouw",
        "0100": "vwo-atheneum onderbouw",
        "0015": "havo/vwo voorbereid. lj",
        "0300": "havo onderbouw",
        "0022": "vmbo/havo voorbereid. lj",
        "0011": "vmbo-gl/tl/havo voorbereid. lj",
        "0046": "vmbo voorbereid. lj lwoo",
        "0023": "vmbo voorbereid. lj",
        "0045": "vmbo-bb/kb voorbereid. lj lwoo",
        "0033": "vmbo-bb/kb voorbereid. lj",
        "0044": "vmbo-gl/tl voorbereid. lj lwoo",
        "0013": "vmbo-gl/tl voorbereid. lj",
        "2210": "vmbo-tl/mavo onderbouw lwoo",
        "0400": "vmbo-tl/mavo onderbouw",
        "0042": "vmbo-gl voorbereid. lj lwoo",
        "0012": "vmbo-gl voorbereid. lj",
        "0043": "vmbo-kb voorbereid. lj lwoo",
        "0032": "vmbo-kb voorbereid. lj",
        "0041": "vmbo-bb voorbereid. lj lwoo",
        "0031": "vmbo-bb voorbereid. lj",
        "1394": "vmbo MTE onderbouw lwoo",
        "1916": "vmbo MTE onderbouw",
        "0273": "vwo-gymnasium cultuur/maat",
        "0272": "vwo-gymnasium economie/maat",
        "0271": "vwo-gymnasium natuur/gezond",
        "0270": "vwo-gymnasium natuur/techniek",
        "0173": "vwo-atheneum cultuur/maat",
        "0172": "vwo-atheneum economie/maat",
        "0171": "vwo-atheneum natuur/gezond",
        "0170": "vwo-atheneum natuur/techniek",
        "0373": "havo cultuur/maatschappij",
        "0372": "havo economie/maatschappij",
        "0371": "havo natuur/gezondheid",
        "0370": "havo natuur/techniek",
        "2213": "vmbo-tl/mavo economie lwoo",
        "0472": "vmbo-tl/mavo economie",
        "2214": "vmbo-tl/mavo groen lwoo",
        "0473": "vmbo-tl/mavo groen",
        "2211": "vmbo-tl/mavo techniek lwoo",
        "0470": "vmbo-tl/mavo techniek",
        "2215": "vmbo-tl/mavo z/prof. lwoo lj3",
        "0474": "vmbo-tl/mavo z/prof. lj3",
        "2212": "vmbo-tl/mavo ZW lwoo",
        "0471": "vmbo-tl/mavo ZW",
        "6075": "vmbo-gl BWI lwoo",
        "6031": "vmbo-gl BWI",
        "6975": "vmbo-gl DP lwoo",
        "6931": "vmbo-gl DP",
        "6475": "vmbo-gl EO lwoo",
        "6431": "vmbo-gl EO",
        "6775": "vmbo-gl groen lwoo",
        "6731": "vmbo-gl groen",
        "6575": "vmbo-gl HBR lwoo",
        "6531": "vmbo-gl HBR",
        "6875": "vmbo-gl MTE lwoo",
        "6831": "vmbo-gl MTE",
        "6375": "vmbo-gl MVI lwoo",
        "6331": "vmbo-gl MVI",
        "6275": "vmbo-gl MTR lwoo",
        "6231": "vmbo-gl MTR",
        "6175": "vmbo-gl PIE lwoo",
        "6131": "vmbo-gl PIE",
        "6675": "vmbo-gl ZW lwoo",
        "6631": "vmbo-gl ZW",
        "6065": "vmbo-kb BWI lwoo",
        "6021": "vmbo-kb BWI",
        "6965": "vmbo-kb DP lwoo",
        "6921": "vmbo-kb DP",
        "6465": "vmbo-kb EO lwoo",
        "6421": "vmbo-kb EO",
        "6765": "vmbo-kb groen lwoo",
        "6721": "vmbo-kb groen",
        "6565": "vmbo-kb HBR lwoo",
        "6521": "vmbo-kb HBR",
        "6865": "vmbo-kb MTE lwoo",
        "6821": "vmbo-kb MTE",
        "6365": "vmbo-kb MVI lwoo",
        "6221": "vmbo-kb MVI",
        "6265": "vmbo-kb MTR lwoo",
        "6321": "vmbo-kb MTR",
        "6165": "vmbo-kb PIE lwoo",
        "6121": "vmbo-kb PIE",
        "6665": "vmbo-kb ZW lwoo",
        "6621": "vmbo-kb ZW",
        "6011": "vmbo-bb BWI",
        "7021": "vmbo-bb BWI entree-opl.",
        "7011": "vmbo-bb BWI leerwerktraj.",
        "6055": "vmbo-bb BWI lwoo",
        "7065": "vmbo-bb BWI entree-opl. lwoo",
        "7055": "vmbo-bb BWI leerwerktraj. lwoo",
        "6911": "vmbo-bb DP",
        "7921": "vmbo-bb DP entree-opl.",
        "7911": "vmbo-bb DP leerwerktraj.",
        "6955": "vmbo-bb DP lwoo",
        "7965": "vmbo-bb DP entree-opl. lwoo",
        "7955": "vmbo-bb DP leerwerktraj. lwoo",
        "6411": "vmbo-bb EO",
        "7421": "vmbo-bb EO entree-opl.",
        "7411": "vmbo-bb EO leerwerktraj.",
        "6455": "vmbo-bb EO lwoo",
        "7465": "vmbo-bb EO entree-opl. lwoo",
        "7455": "vmbo-bb EO leerwerktraj. lwoo",
        "6711": "vmbo-bb groen",
        "7721": "vmbo-bb groen entreeopl.",
        "7711": "vmbo-bb groen leerwerktraj.",
        "6755": "vmbo-bb groen lwoo",
        "7765": "vmbo-bb groen entree-opl. lwoo",
        "7755": "vmbo-bb groen leerwerktraj. lwoo",
        "6511": "vmbo-bb HBR",
        "7521": "vmbo-bb HBR entree-opl.",
        "7511": "vmbo-bb HBR leerwerktraj.",
        "6555": "vmbo-bb HBR lwoo",
        "7565": "vmbo-bb HBR entree-opl. lwoo",
        "7555": "vmbo-bb HBR leerwerktraj. lwoo",
        "6811": "vmbo-bb MTE",
        "7821": "vmbo-bb MTE entree-opl.",
        "7811": "vmbo-bb MTE leerwerktraj.",
        "6855": "vmbo-bb MTE lwoo",
        "7865": "vmbo-bb MTE entree-opl. lwoo",
        "7855": "vmbo-bb MTE leerwerktraj. lwoo",
        "6311": "vmbo-bb MVI",
        "7321": "vmbo-bb MVI entree-opl.",
        "7311": "vmbo-bb MVI leerwerktraj.",
        "6355": "vmbo-bb MVI lwoo",
        "7365": "vmbo-bb MVI entree-opl. lwoo",
        "7355": "vmbo-bb MVI leerwerktraj. lwoo",
        "6211": "vmbo-bb MTR",
        "7221": "vmbo-bb MTR entree-opl.",
        "7211": "vmbo-bb MTR leerwerktraj.",
        "6255": "vmbo-bb MTR lwoo",
        "7265": "vmbo-bb MTR entree-opl. lwoo",
        "7255": "vmbo-bb MTR leerwerktraj. lwoo",
        "6111": "vmbo-bb PIE",
        "7121": "vmbo-bb PIE entree-opl.",
        "7111": "vmbo-bb PIE leerwerktraj.",
        "6155": "vmbo-bb PIE lwoo",
        "7165": "vmbo-bb PIE entree-opl. lwoo",
        "7155": "vmbo-bb PIE leerwerktraj. lwoo",
        "6611": "vmbo-bb ZW",
        "7621": "vmbo-bb ZW entree-opl.",
        "7611": "vmbo-bb ZW leerwerktraj.",
        "6655": "vmbo-bb ZW lwoo",
        "7665": "vmbo-bb ZW entree-opl. lwoo",
        "7655": "vmbo-bb ZW leerwerktraj. lwoo",
        "4021": "vwo-gymnasium vavo",
        "4026": "vwo-gymnasium vavo na gezakt",
        "4027": "vwo-gymnasium vavo na geslaagd",
        "4011": "vwo-atheneum vavo",
        "4016": "vwo-atheneum vavo na gezakt",
        "4017": "vwo-atheneum vavo na geslaagd",
        "4031": "havo vavo",
        "4036": "havo vavo na gezakt",
        "4037": "havo vavo na geslaagd",
        "4040": "vmbo-tl vavo",
        "4045": "vmbo-tl vavo na gezakt",
        "4046": "vmbo-tl vavo na geslaagd",
        "4050": "vmbo-tl vavo lwoo",
        "4055": "vmbo-tl vavo lwoo na gezakt",
        "4056": "vmbo-tl vavo lwoo na geslaagd"
    }

    def __init__(self):
        pass

    @staticmethod
    def get_opleiding(elementcode: str) -> str or None:
        try:
            return ElementcodeOpleiding.ELEMENTCODES[elementcode]
        except KeyError:
            return None

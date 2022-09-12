#Giant List of words for the computer to choose from
#formatted in [letter][word]
#32 words for each letter

#used the aid of:
#google docs (temporary storage of word) [https://docs.google.com]
#http://www.unit-conversion.info/texttools/replace-text/ (formatting)
#https://www.textfixer.com/tools/remove-line-breaks.php (formatting)
#https://randomwordgenerator.com (random word generator)
#https://www.crosswordsolver.org/x-words (words for letters k,x,y, and z)
potentialWords = [
  ["acute", "approach", "applied", "autonomy", "achievement", "abandon", "ambition", "aloof", "allocation", "appointment", "assessment", "attention", "authority", "abridge", "anticipation", "artist", "acquaintance", "advertise", "aspect", "avenue", "attack", "adjust", "argument", "advance", "application", "appoint", "advantage", "appetite", "action", "average", "anger", "automatic"],
  
  ["bless", "broadcast", "burn", "beam", "bare", "bake", "black", "biology", "brake", "bread", "book", "brush", "buttocks", "boat", "branch", "breast", "bird", "banana", "bride", "brave", "blade", "begin", "beef", "background", "burst", "battle", "blind", "baseball", "board", "bottom", "birthday", "biscuit"], 
  
  ["chest", "cultivate", "coin", "cool", "cruel", "census", "cord", "casualty", "charity", "convulsion", "circulate", "change", "crouch", "culture", "corner", "copper", "conductor", "courtesy", "commission", "conscience", "consideration", "comfort", "copyright", "character", "code", "compliance", "choose", "cottage", "conventional", "characteristic", "concession", "classify"],
  
  ["deep", "dull", "differ", "dance", "deliver", "demonstrator", "deficiency", "dominant", "designer", "determine", "discount", "delay", "document", "dough", "dynamic", "disgrace", "desire", "dedicate", "district", "draw", "depart", "decrease", "dependence", "dine", "domination", "dismissal", "damage", "duke", "drug", "door", "demonstrate", "departure"],

  ["earthwax", "episode", "examination", "earthquake", "excess", "energy", "ecstasy", "expertise", "establish", "exhibition", "embryo", "equinox", "election", "evaluate", "edge", "earth", "extreme", "exact", "economy", "execute", "enthusiasm", "emotion", "entertainment", "employee", "ethics", "exercise", "elapse", "eliminate", "expect", "evoke", "experiment", "enlarge"],

  ["full", "feed", "flower", "fold", "fireplace", "forward", "fortune", "familiar", "freedom", "football", "foreigner", "frequency", "finished", "flesh", "fame", "flavor", "falsify", "friend", "foster", "flight", "formation", "forestry", "fate", "free", "finger", "fire", "fade", "food", "flock", "favor", "friendly", "fall"],

  ["garlic", "girl", "grandmother", "gradual", "ghostwriter", "giant", "generate", "glory", "guest", "governor", "guitar", "galaxy", "gold", "glare", "grace", "ghost", "gregarious", "graphic", "genetic", "glide", "glove", "guideline", "growth", "grind", "ground", "glasses", "grand", "grudge", "gloom", "guard", "grateful", "grounds"],

  ["hierarchy", "heal", "heroin", "huge", "half", "home", "hesitate", "harvest", "hour", "halt", "heat", "honest", "helicopter", "hilarious", "hardship", "highway", "hook", "hypothesize", "hurl", "homosexual", "horse", "hair", "hang", "honor", "hobby", "houseplant", "highlight", "have", "hemisphere", "helmet", "harbor", "habitinjury"],

  ["immune", "iron", "item", "invite", "integrated", "indoor", "identity", "implicit", "instrument", "insurance", "intermediate", "incongruous", "intensify", "instal", "inspector", "institution", "innocent", "inquiry", "inhibition", "ideal", "injection", "indirect", "integrity", "insight", "import", "intelligence", "impact", "ignorant", "information", "intention", "interrupt"],

  ["jabot", "jacal", "jacks", "jacky", "jaded", "jades", "jager", "jaggs", "jaggy", "jagran", "jails", "jakes", "jalap", "jalopnik", "jambe", "jambs", "jammy", "janes", "janty", "japan", "japed", "japer", "japes", "jarls", "jatos", "jauks", "jaunt", "jaups", "javas", "jawan", "jawed", "jazzy"],

  ["kaas", "kabs", "kadi", "kaes", "kafs", "kagu", "kaif", "kail", "kain", "kaka", "kaki", "kale", "kame", "kami", "kana", "kane", "kaon", "kapa", "kaph", "kapu", "karn", "kart", "kata", "kats", "kava", "kayo", "kays", "kbar", "keas", "keck", "keef", "keek"],

  ["lose", "latest", "love", "lodge", "lost", "line", "launch", "limit", "loop", "lemon", "laundry", "legend", "liberty", "linger", "legislature", "live", "landscape", "license", "lawyer", "lounge", "liability", "leadership", "lily", "locate", "light", "lamb", "lion", "litigation", "listen", "length", "link", "lighter"],

  ["miserable", "mayor", "mountain", "microphone", "meadow", "meet", "minimize", "medal", "moral", "mile", "monstrous", "mask", "morale", "movie", "morning", "magnitude", "motif", "misplace", "machinery", "mathematics", "miner", "musical", "moving", "mutual", "muscle", "margin", "manual", "meaning", "mushroom", "minute", "motorcycle", "mess"],

  ["novel", "news", "normal", "number", "national", "necklace", "negotiation", "nationalist", "note", "native", "needle", "name", "norm", "nomination", "neck", "nail", "notebook", "neighborhood", "noise", "nonsense", "nuance", "nervous", "nose", "neutral", "nature", "need", "north", "notion", "nest", "noble", "nuclear", "node"],

  ["opponent", "organisation", "offset", "occupy", "office", "onion", "operation", "obese", "offend", "outlook", "oven", "observation", "obstacle", "opinion", "opera", "outlet", "ostracize", "orbit", "order", "opposite", "organ", "overall", "offender", "open", "outside", "opposed", "origin", "orange", "occupation", "offer", "original", "object"],

  ["prefer", "pawn", "photograph", "posture", "priority", "pocket", "paper", "producer", "peanut", "precede", "poison", "paralyzed", "pavement", "power", "panel", "profound", "promote", "provincial", "play", "perception", "parallel", "premature", "psychology", "private", "public", "paint", "prevalence", "policeman", "publicity", "perfume", "projection", "penalty"],

  ["quake", "qualm", "quark", "quipu", "quirk", "qibla", "qubit", "quims", "quips", "quags", "quash", "quays", "quell", "query", "quiz", "qoph", "quem", "quim", "quip", "quag", "quay", "quey", "quad", "quid", "quin", "quod", "qadi", "qaid", "quai", "quit", "quoi", "qats"],

  ["recruit", "resident", "related", "reception", "room", "recommendation", "runner", "restrain", "restoration", "respect", "represent", "recession", "reptile", "route", "relief", "requirement", "regard", "rich", "ridge", "rehearsal", "rape", "record", "rehabilitation", "realize", "reinforce", "realism", "referee", "role", "rack", "redeem", "recycle", "rabbit"],

  ["sugar", "seller", "sympathetic", "science", "seed", "salad", "screen", "suggest", "scenario", "sail", "spectrum", "separation", "scrap", "situation", "salesperson", "straighten", "seek", "shop", "sleeve", "stir", "summary", "stable", "similar", "staircase", "supply", "safari", "shift", "skilled", "speed", "shark", "security", "save"],

  ["torture", "troop", "ticket", "title", "team", "tablet", "turkey", "tail", "touch", "tight", "triangle", "terms", "tune", "theft", "trail", "temptation", "threshold", "truck", "trolley", "tiptoe", "tolerate", "tract", "trouble", "tape", "track", "tent", "theory", "theme", "thumb", "tempt", "throw", "thank"],

  ["upset", "underline", "uniform", "urge", "uncertainty", "unfortunate", "undertake", "utter", "undress", "unanimous", "union", "unique", "update", "understand", "user", "unity", "urgency", "unpleasant", "unrest", "unlawful", "uncle", "unlike", "understanding", "useful", "urine", "unaware", "unlikely", "unfair", "umbrella", "undermine", "unit"],

  ["volunteer", "vacuum", "value", "vision", "victory", "version", "voucher", "village", "venture", "vegetation", "vain", "voter", "veteran", "valid", "visible", "verdict", "volcano", "variable", "visual", "vague", "velvet", "valley", "virtue", "viable", "volume", "vein", "vertical", "variation", "vessel", "Venus", "veil", "vigorous"],

  ["woman", "withdrawal", "wardrobe", "word", "weight", "work", "wound", "willpower", "wagon", "wilderness", "walk", "weigh", "wash", "wonder", "writer", "waist", "warm", "wind", "world", "whole", "wing", "whip", "weapon", "week", "wheel", "witness", "widen", "wait", "will", "wild", "welfare", "wreck"],

  ["xebecs", "xylems", "xylyls", "xylans", "xylene", "xyloid", "xylols", "xylose", "xystus", "xenial", "xenons", "xoanon", "xyster", "xystoi", "xystos", "xenias", "xerox", "xebec", "xylem", "xylyl", "xylan", "xylol", "xeric", "xenon", "xysti", "xysts", "xenia", "xerus", "xoana", "xyst", "xes", "xis"],

  ["yag", "yah", "yak", "yam", "yap", "yar", "yas", "yaw", "yay", "yea", "yeh", "yen", "yep", "yes", "yet", "yew", "yin", "yip", "yob", "yod", "yok", "yom", "yon", "you", "yow", "yuk", "yum", "yup", "yack", "yaff", "yage", "yagi"],

  ["zaire", "zamia", "zanza", "zappy", "zarfs", "zaxes", "zayin", "zazen", "zeals", "zebec", "zebra", "zebus", "zeins", "zerks", "zeros", "zests", "zesty", "zetas", "zibet", "zilch", "zills", "zincs", "zincy", "zineb", "zines", "zings", "zingy", "zinky", "zippy", "ziram", "zitis", "zizit"]]
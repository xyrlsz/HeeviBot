from nonebot import on_command
from nonebot.rule import to_me
from nonebot.matcher import Matcher
from nonebot.adapters import Event
from nonebot.params import Message
from nonebot.exception import MatcherException
from .trigram_work import TianDi

Trigram = on_command("起卦", rule=to_me(), aliases={"八卦","算卦","卦象"}, priority=10, block=True)

@Trigram.handle()
async def handle_Trigram(matcher:Matcher,args=Message) :
    try :
        Hexa_Trigram_Orgin , Hexa_Trigram_Change = TianDi()
        await Trigram.finish('{}变卦{}'.format(Hexa_Trigram_Orgin,Hexa_Trigram_Change))
    except MatcherException :
        raise
    except Exception as e :
        pass


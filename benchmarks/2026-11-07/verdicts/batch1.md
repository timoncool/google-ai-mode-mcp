########## QUESTION q01 ##########
Question: Which RFC defines HTTP/3, and over which transport protocol does it run?
Reference answer: RFC 9114; it runs over QUIC (RFC 9000).
Reference source: https://www.rfc-editor.org/rfc/rfc9114

=== OUTPUT X84 ===
**HTTP/3 is defined by** **[RFC 9114](https://www.rfc-editor.org/info/rfc9114/)** **and runs over the QUIC transport protocol.** [1]

Published by the Internet Engineering Task Force (IETF) in June 2022, HTTP/3 departs from earlier versions of HTTP that relied on TCP. [2]

-   **Transport Layer:** HTTP/3 maps HTTP semantics directly onto **QUIC** (defined in [RFC 9000](https://www.rfc-editor.org/info/rfc9000/)), which itself runs on top of **UDP** (User Datagram Protocol) rather than TCP. [4]
    
-   **Built-in Encryption:** Unlike older versions where TLS was layered separately over TCP, QUIC integrates **TLS 1.3** directly into the transport handshake. [5]
    
-   **Header Compression:** Because QUIC streams can arrive out of order, HTTP/3 replaces HTTP/2's HPACK compression with **QPACK** (defined in [RFC 9204](https://www.rfc-editor.org/info/rfc9204/)). [7]
    

Would you like to compare **HTTP/3 and HTTP/2** in terms of performance, or explore how **QUIC eliminates head-of-line blocking**?

Sources:
1. https://www.rfc-editor.org/info/rfc9114/
2. https://icannwiki.org/HTTP/3
3. https://www.rfc-editor.org/info/rfc9000/
4. https://www.linkedin.com/posts/the-tech-firm_quic-explained-why-rfc-9000-changed-internet-activity-7500553479388688384-C58a
5. https://datatracker.ietf.org/doc/draft-ietf-quic-http/23/
6. https://www.rfc-editor.org/info/rfc9204/
7. https://ma.ttias.be/quic-http3-in-2026/
=== END OF OUTPUT X84 ===

=== OUTPUT Z95 ===
Title: RFC 9114: HTTP/3
URL: https://www.rfc-editor.org/rfc/rfc9114.html
Published: 2022-06-03T00:00:00.000Z
Author: Mike Bishop
Highlights:
RFC 9114: HTTP/3

## Abstract

The QUIC transport protocol has several features that are desirable in a transport for HTTP, such as stream multiplexing, per-stream flow control, and low-latency connection establishment. This document describes a mapping of HTTP semantics over QUIC. This document also identifies HTTP/2 features that are subsumed by QUIC and describes how HTTP/2 extensions can be ported to HTTP/3.¶

...

HTTP semantics ([HTTP]) are used for a broad range of services on the Internet. These semantics have most commonly been used with HTTP/1.1 and HTTP/2. HTTP/1.1 has been used over a variety of transport and session layers, while HTTP/2 has been used primarily with TLS over TCP. HTTP/3 supports the same semantics over a new transport protocol: QUIC.¶

...

### 1.2. Delegation to QUIC 

The QUIC transport protocol incorporates stream multiplexing and per-stream flow control, similar to that provided by the HTTP/2 framing layer. By providing reliability at the stream level and congestion control across the entire connection, QUIC has the capability to improve the performance of HTTP compared to a TCP mapping. QUIC also incorporates TLS 1.3 ([TLS]) at the transport layer, offering comparable confidentiality and integrity to running TLS over TCP, with the improved connection setup latency of TCP Fast Open ([TFO]).¶

This document defines HTTP/3: a mapping of HTTP semantics over the QUIC transport protocol, drawing heavily on the design of HTTP/2. HTTP/3 relies on QUIC to provide confidentiality and integrity protection of data; peer authentication; and reliable, in-order, per-stream delivery. While delegating stream lifetime and flow-control issues to QUIC, a binary framing similar to the HTTP/2 framing is used on each stream. Some HTTP/2 features are subsumed by QUIC, while other features are implemented atop QUIC.¶

QUIC is described in [QUIC-TRANSPORT]. For a full description of HTTP/2, see [HTTP/2].¶

## 2. HTTP/3 Protocol Overview 

HTTP/3 provides a transport for HTTP semantics using the QUIC transport protocol and an internal framing layer similar to HTTP/2.¶

Once a client knows that an HTTP/3 server exists at a certain endpoint, it opens a QUIC connection. QUIC provides protocol negotiation, stream-based multiplexing, and flow control. Discovery of an HTTP/3 endpoint is described in Section 3.1.¶

...

Multiplexing of requests is performed using the QUIC stream abstraction, which is described in Section 2 of [QUIC-TRANSPORT]. Each request-response pair consumes a single QUIC stream. Streams are independent of each other, so one stream that is blocked or suffers packet loss does not prevent progress on other streams.¶

...

HTTP/3 relies on QUIC version 1 as the underlying transport. The use of other QUIC transport versions with HTTP/3 MAY be defined by future specifications.¶

QUIC version 1 uses TLS version 1.3 or greater as its handshake protocol.

---

Title: HTTP/3
URL: https://en.wikipedia.org/wiki/HTTP/3
Published: 2026-11-04T07:02:58.000Z
Author: N/A
Highlights:
HTTP/3

| International standard | RFC 9114 [1] (HTTP/3 also uses the completed QUIC protocol described in RFC 9000 and related RFCs such as RFC 9001) |
| --- | --- |
| Developed by | IETF |
| Introduced | June 2022 |
| Website | https://httpwg.org/specs/rfc9114.html |

HTTP/3 is the third major version of the Hypertext Transfer Protocol used to exchange information on the World Wide Web, complementing the widely deployed HTTP/1.1 and HTTP/2. Unlike previous versions which relied on the well-established TCP (published in 1974), [2] HTTP/3 uses QUIC (officially introduced in 2021), [3] a multiplexed transport protocol built on UDP. [4]

...

HTTP semantics are consistent across versions: the same request methods, status codes, and message fields are typically applicable to all versions. The differences are in the mapping of these semantics to underlying transports. Both HTTP/1.1 and HTTP/2 use TCP as their transport. HTTP/3 uses QUIC, a transport layer network protocol which uses user space congestion control over the User Datagram Protocol (UDP). The switch to QUIC aims to fix a major problem of HTTP/2 called " head-of-line blocking": because the parallel nature of HTTP/2's multiplexing is not visible to TCP's loss recovery mechanisms, a lost or reordered packet causes all active transactions to experience a stall regardless of whether that transaction was impacted by the lost packet. Because QUIC provides native multiplexing, lost packets only impact the streams where data has been lost.

---

Title: What is HTTP/3?
URL: https://www.cloudflare.com/learning/performance/what-is-http3/
Published: N/A
Author: N/A
Highlights:
An important difference in HTTP/3 is that it runs on QUIC, a new transport protocol. QUIC is designed to be fast and to support switching rapidly between networks. It relies on the User Datagram Protocol (UDP) rather than the Transmission Control Protocol (TCP), which mitigates an issue called head-of-line blocking in TCP, where network packet loss or reordering can slow down high-transaction connections. Furthermore, QUIC separates out the layer 4 transport connection from the layer 3 IP flow, allowing for migration between different networks without disruption.

---

Title: RFCs about HTTP/3 | RFC Editor
URL: https://www.rfc-editor.org/subjects/http3/
Published: N/A
Author: N/A
Highlights:
- ### RFC 9114: HTTP/3

Proposed Standard
...
- June 2022
- IETF publication
- Web and Internet Transport
...
#### Abstract 

The QUIC transport protocol has several features that are desirable in a transport for HTTP, such as stream multiplexing,

---

Title: What Are HTTP/3 and QUIC Proxies? | SparkProxy
URL: https://www.sparkproxy.io/blog/what-are-http3-and-quic-proxies
Published: 2026-08-25T04:30:02.000Z
Author: N/A
Highlights:
RFC 9000, published May 2021. It rides on UDP, folds TLS 1.3 into the transport handshake (RFC 9001), and provides its own streams, flow control, and loss recovery. HTTP/3, ... HTTP semantics layer that runs over QUIC. Its ALPN token is the string `h3`.

---

Title: draft-ietf-quic-http-34 - HTTP/3
URL: https://datatracker.ietf.org/doc/draft-ietf-quic-http/34/
Published: N/A
Author: Mike Bishop
Highlights:
The information below is for an old version of the document that is already published as an RFC. 

| Document | Type | This is an older version of an Internet-Draft that was ultimately published as RFC 9114. |
| --- | --- | --- |
| | Author | Mike Bishop (mbishop%40evequefou.be) |
| | Last updated | 2022-09-27 (Latest revision 2021-02-02) |
| | Replaces | draft-shade-quic-http2-mapping |
| | RFC stream | Internet Engineering Task Force (IETF) |
| | Intended RFC status | Proposed Standard |
| | Formats | txt html xml htmlized bibtex bibxml |
| | Reviews | GENART Telechat review (of -33) by Reese Enghardt Ready SECDIR IETF Last Call review (of -32) by Hilarie Orman Ready GENART IETF Last Call review (of -32) by Reese Enghardt Ready w/issues |
| | Additional resources | Mailing list discussion |
| Stream | WG state | Submitted to IESG for Publication |
| | Document shepherd | Lucas Pardue (lucas%40lucaspardue.com) |
| | Shepherd write-up | Show Last changed 2020-09-25 |
| IESG | IESG state | Became RFC 9114 (Proposed Standard) |
| | Action Holders | (None) |
| | Consensus boilerplate | Yes |
| | Telechat date | (None) |
| | Responsible AD | Zaheduzzaman Sarker (zahed.sarker.ietf%40gmail.com) |
| | Send notices to | quic-chairs@ietf.org |
| IANA | IANA review state | Version Changed - Review Needed |
| | IANA action state | RFC-Ed-Ack |
| | IANA expert review state | Expert Reviews OK |

...

The QUIC transport protocol has several features that are desirable
   in a transport for HTTP, such as stream multiplexing, per-stream flow
   control, and low-latency connection establishment.  This document
   describes a mapping of HTTP semantics over QUIC.  This document also
   identifies HTTP/2 features that are subsumed by QUIC, and describes
   how HTTP/2 extensions can be ported to HTTP/3.

...

HTTP/1.1 has been used over a variety of

...

HTTP/3 supports the same semantics over a new
   transport protocol, QUIC.

...

The QUIC transport protocol incorporates stream multiplexing and per-
   stream flow control, similar to that provided by the HTTP/2 framing
   layer.  By providing reliability at the stream level and congestion
   control across the entire connection, QUIC has the capability to
   improve the performance of HTTP compared to a TCP mapping.  QUIC also
   incorporates TLS 1.3 ([TLS13]) at the transport layer, offering
   comparable confidentiality and integrity to running TLS over TCP,
   with the improved connection setup latency of TCP Fast Open ([TFO]).

   This document defines HTTP/3, a mapping of HTTP semantics over the
   QUIC transport protocol, drawing heavily on the design of HTTP/2.
   HTTP/3 relies on QUIC to provide confidentiality and integrity
   protection of data; peer authentication; and reliable, in-order, per-
   stream delivery.  While delegating stream lifetime and flow control
   issues to QUIC, a binary framing similar to the HTTP/2 framing is
   used on each stream.  Some HTTP/2 features are subsumed by QUIC,
   while other features are implemented atop QUIC.

---

Title: HTTP/3 in Practice — HTTP/3
URL: https://www.andy-pearce.com/blog/posts/2023/Apr/http3-in-practice-http3/
Published: 2023-04-13T08:30:00.000Z
Author: Andy Pearce
Highlights:
HTTP/3 was released most recently, its very first draft being released at the end ... 2016 under the title “ HTTP over QUIC”, and being referred to as HTTP/ ... from the end of 2018. It became a full Standards Track RFC

---

Title: RFC 9114: HTTP/3 | Guide books
URL: https://dl.acm.org/doi/abs/10.17487/RFC9114
Published: 2022-06-01T00:00:00.000Z
Author: Editor : M. Bishop
Highlights:
# RFC 9114: HTTP/3

June 2022

Editor: M. Bishop

Publisher:

RFC Editor, United States

Published: 01 June 2022 

## Abstract

The QUIC transport protocol has several features that are desirable in a transport for HTTP, such as stream multiplexing, per-stream flow control, and low-latency connection establishment. This document describes a mapping of HTTP semantics over QUIC. This document also identifies HTTP/2 features that are subsumed by QUIC and describes how HTTP/2 extensions can be ported to HTTP/3.

---

Title: What Is HTTP/3? A Technical Guide to QUIC, Streams and Real-World Deployment - DED9
URL: https://ded9.com/what-is-http-3-a-technical-guide-to-quic-streams-and-real-world-deployment/
Published: 2026-08-20T09:09:14.000Z
Author: Erfan
Highlights:
HTTP/3 is the third major revision of the Hypertext Transfer Protocol, standardized as RFC 9114 in June 2022. Its defining change is not in HTTP semantics—methods, status codes, and header fields are the same as those defined in RFC 9110—but in the transport underneath. HTTP/1.1 and HTTP/2 run over TCP. HTTP/3 runs over QUIC (RFC 9000), a connection-oriented, encrypted transport built on UDP.

---

Title: HTTP/3: Browser Support, Features, Known Issues
URL: https://www.testmuai.com/learning-hub/http3-browser-support/
Published: N/A
Author: N/A
Highlights:
HTTP/3 is the third major version of the Hypertext Transfer Protocol, standardized by the IETF in RFC 9114, that runs HTTP semantics over the QUIC transport protocol on UDP. It supports
...
TLS 1.3 encryption, and congestion control into one layer, which
=== END OF OUTPUT Z95 ===

=== OUTPUT Z62 ===
HTTP/3 is defined in **RFC 9114**, published in June 2022 as a Standards Track document by Mike Bishop. It runs over **QUIC**, not TCP. The RFC describes HTTP semantics mapped onto QUIC a mapping of HTTP semantics over the QUIC transport protocol, drawing heavily on the design of HTTP/2.

Some supporting detail from the results:
- The RFC notes that earlier versions relied on TCP. HTTP/2 has been used primarily with TLS over TCP.
- QUIC supplies the transport features HTTP/3 depends on, including stream multiplexing and flow control. QUIC provides protocol negotiation, stream-based multiplexing, and flow control.
- QUIC itself is specified separately in RFC 9000, which an IPFYI summary of RFC 9114 confirms the mapping of HTTP semantics onto QUIC (RFC 9000).

Sources:
1. https://www.ietf.org/ietf-ftp/rfc/rfc9114.pdf
2. https://www.rfc-editor.org/v3test/rfc9114v3.pdf
3. https://datatracker.ietf.org/doc/html/rfc9114/
4. https://ftp.kaist.ac.kr/rfc/rfc9114.pdf
5. https://datatracker.ietf.org/doc/rfc9114/
6. https://www.rfc-editor.org/v3test/rfc9114.pdf
7. https://ipfyi.com/rfc/9114/
=== END OF OUTPUT Z62 ===


########## QUESTION q02 ##########
Question: С какой версии Python порядок вставки ключей в dict гарантирован спецификацией языка?
Reference answer: Python 3.7 (in 3.6 it was a CPython implementation detail).
Reference source: https://docs.python.org/3/whatsnew/3.7.html

=== OUTPUT C43 ===
Порядок вставки ключей гарантирован спецификацией языка начиная с **Python 3.7**. Поиск подтверждает это в нескольких источниках.

- **Python 3.7:** одно из обсуждений на python-dev фиксирует решение, что порядок вставки в dict становится частью языка (From Python 3.7: the insertion-order preservation nature of dict objects has been declared to be an official part of the Python language spec.).
- **Python 3.6:** порядок уже сохранялся в CPython, но считался деталью реализации, а не гарантией языка. Другие реализации, например PyPy и Jython, на это не опирались (Important: This was only guaranteed in CPython, not in other Python implementations like PyPy or Jython.).
- **Python 3.5 и ниже:** порядок не гарантировался вовсе.

Итог: полагаться на порядок можно в любой совместимой реализации начиная с 3.7. В 3.6 он работал в CPython, но переносимым контрактом не был.

Sources:
1. https://mail.python.org/pipermail/python-dev/2017-December/151325.html
2. https://codemia.io/knowledge-hub/path/the_order_of_elements_in_dictionary
3. https://pyguide.pages.dev/qa/are-python-dictionaries-ordered-explained
4. https://pyguide.pages.dev/qa/are-python-dictionaries-ordered-questions
5. https://codemia.io/knowledge-hub/path/are_dictionaries_ordered_in_python_36
6. https://discuss.python.org/t/are-dict-class-dictionaries-ordered/38172
7. https://pyguide.pages.dev/tutorials/python-dictionary-ordering-guide
=== END OF OUTPUT C43 ===

=== OUTPUT I10 ===
Сохранение порядка вставки ключей в `dict` гарантировано спецификацией языка начиная с версии **Python 3.7**. [1]

История этого изменения по версиям:

-   **Python 3.6:** Сохранение порядка впервые появилось в стандартной реализации CPython как побочный эффект новой компактной структуры словарей, но официально считалось лишь деталью реализации.
    
-   **Python 3.7:** Поведение закрепили в спецификации языка как обязательный стандарт для всех реализаций Python.
    
-   **До Python 3.6:** Порядок элементов не сохранялся; для этих задач использовался класс `collections.OrderedDict`. [2]
    

Если вам нужно сравнить возможности обычного `dict` и `collections.OrderedDict` (например, различия в сравнении словарей и специальных методах), я могу разобрать их в деталях. Хотите узнать подробнее?

Sources:
1. https://thelightech.ru/blog/razrabotchikam/kak-pomenyat-klyuchi-i-znacheniya-v-slovare-python/
2. https://sky.pro/wiki/python/uporyadochivaem-slovari-v-python-sokhranyaem-poryadok-elementov/
=== END OF OUTPUT I10 ===

=== OUTPUT X14 ===
Title: What’s New In Python 3.7 — Python 3.15.2 documentation
URL: https://docs.python.org/3/whatsnew/3.7.html
Published: N/A
Author: N/A
Highlights:
Python data model improvements:

- PEP 562, customization of access to module attributes.
- PEP 560, core support for typing module and generic types.
- the insertion-order preservation nature of dict objects has been declared to be an official part of the Python language spec.

---

Title: Issue 39879: Update language reference to specify that dict is insertion-ordered. - Python tracker
URL: https://bugs.python.org/issue39879
Published: N/A
Author: N/A
Highlights:
| Title: | Update language reference to specify that dict is insertion-ordered. | | |
| --- | --- | --- | --- |
| Type: | | Stage: | resolved |
| Components: | Documentation | Versions: | Python 3.9, Python 3.8, Python 3.7 |

...

| Messages (14) | | |
| --- | --- | --- |
| msg363533 - (view) | Author: Eric Snow (eric.snow) * | Date: 2020-03-06 18:33 |
| As of 3.7 [1], dict is guaranteed to preserve insertion order: the insertion-order preservation nature of dict objects has been declared to be an official part of the Python language spec. However, at least one key part of the language reference [2] was not updated to reflect this: "3.2. The standard type hierarchy" > "Mappings" > "Dictionaries". Note that the library docs [3] *were* updated. [1] https://docs.python.org/3/whatsnew/3.7.html#summary-release-highlights [2] https://docs.python.org/3/reference/datamodel.html#index-30 [3] https://docs.python.org/3/library/stdtypes.html#typesmapping | | |
| msg364204 - (view) | Author: Lahfa Samy (AkechiShiro) * | Date: 2020-03-14 22:28 |
| Hi, I would like to take this issue as my first contribution to Python, I'm currently subscribed to the python-core-mentorship list. I do not know exactly how to submit a patch for an issue. Kind regards. | | |
| msg364206 - (view) | Author: Mariatta (Mariatta) * | Date: 2020-03-14 22:32 |
| Patch are submitted as pull request on our GitHub repo. Here's a write-up on how to do it https://devguide.python.org/pullrequest/#step-by-step-guide | | |
| msg364229 - (view) | Author: Lahfa Samy (AkechiShiro) * | Date: 2020-03-15 12:01 |
| Following the guide, I've send a patch with the fix, I'm waiting for a review. Once the patch will be reviewed and accepted. My patch will need to be backported from 3.9 to 3.7. | | |
| msg364303 - (view) | Author: Furkan Onder (furkanonder) * | Date: 2020-03-16 09:43 |
| I sent pr. All tests passed successfully. If accepted, this will be my first contribution :) https://github.com/python/cpython/pull/19027 | | |
| msg364484 - (view) | Author: Zachary Ware (zach.ware) * | Date: 2020-03-17 22:02 |
| Hi Furkan. Please note that Lahfa Samy had already submitted a PR for this issue after "claiming" it with a note here; proper "netiquette" suggests not jumping in with your own PR in such a situation. Fortuitously though, it looks like the both of you have actually implemented about half of the final change that we need here :). I'll be leaving review comments on both PRs; I recommend that the two of you work together to combine your PRs into a single PR with both of your (revised) changes. | | |
| msg364494 - (view) | Author: Lahfa Samy (AkechiShiro) * | Date: 2020-03-18 01:33 |
| Hi Furkan, would you mind to combine your revised PR with mine so that we can do as suggested by Zachary? | | |
| msg364502 - (view) | Author: Furkan Onder (furkanonder) * | Date: 2020-03-18 07:26 |
| Hello Samy, I sent you pr from the docs-dict-ordered branch in your cpython repository. Now both of us have merged pr. I closed my own pr. You can also close your pr and send these changes again as bpo-39879. It's my pr, https://github.com/AkechiShiro/cpython/pull/1 | | |
| msg364520 - (view) | Author: Lahfa Samy (AkechiShiro) * | Date: 2020-03-18 14:08 |
| Thank you for your quick work, I have successfully merged your changes in the branch of the first PR, now awaiting review from Zachary. | | |
| msg365080 - (view) | Author: Zachary Ware (zach.ware) * | Date: 2020-03-26 14:54 |
| New changeset 59c644eaa72b0cc48302f59d66852c4ea8332eba by Lahfa Samy in branch 'master': bpo-39879: Update datamodel docs to include dict ordering (GH-19006) https://github.com/python/cpython/commit/59c644eaa72b0cc48302f59d66852c4ea8332eba | | |
| msg365081 - (view) | Author: miss-islington (miss-islington) | Date: 2020-03-26 14:59 |
| New changeset ea0eeb8d3a0544334f8836c98a761b2e3df2bd94 by Miss Islington (bot) in branch '3.7': bpo-39879: Update datamodel docs to include dict ordering (GH-19006) https://github.com/python/cpython/commit/ea0eeb8d3a0544334f8836c98a761b2e3df2bd94 | | |
| msg365082 - (view) | Author: miss-islington (miss-islington) | Date: 2020-03-26 15:00 |
| New changeset 96686c761d0587080effc113367431a0d396eb45 by Miss Islington (bot) in branch '3.8': bpo-39879: Update datamodel docs to include dict ordering (GH-19006) https://github.com/python/cpython/commit/96686c761d0587080effc113367431a0d396eb45 | | |
| msg365083 - (view) | Author: Zachary Ware (zach.ware) * | Date: 2020-03-26 15:01 |
| Thanks for the patch! | | |
| msg365085 - (view) | Author: STINNER Victor (vstinner) * | Date: 2020-03-26 15:19 |
| What's New in Python 3.7 says: > the insertion-order preservation nature of dict objects has been declared to be an official part of the Python language spec. Reference: https://mail.python.org/pipermail/python-dev/2017-December/151283.html I just wanted to add a reference for this change. I wanted to check if it is ok to modify the doc: yes, it is :-) | | |

---

Title: Why dict ordering became a language guarantee — How to Python
URL: https://www.howtopython.com/a/dict-ordering
Published: 2026-05-11T00:00:00.000Z
Author: N/A
Highlights:
d = {}
d["c"] = 1
d["a"] = 2
d["b"] = 3
list(d)         # ['c', 'a', 'b']

...

Insertion order, preserved exactly. Run the same code in Python 3.5 and you'd get whatever order the hash table felt like — `['a', 'b', 'c']`, or `['b', 'c', 'a']`, or something else depending on the build, the keys, and the phase of the moon.

...

## From "implementation detail" to language guarantee

When CPython 3.6 shipped, the release notes called dict ordering an "implementation detail" — meaning don't rely on it, we might change it. But everyone immediately started relying on it, because of course they did. And the new layout was clearly better than the old one. Reverting it would have meant giving up the memory savings.

So in Python 3.7, the language reference was updated:

> the insertion-order preservation nature of dict objects has been declared to be an official part of the Python language spec.

Every conforming Python implementation now has to preserve insertion order. CPython, PyPy, MicroPython, Jython, whatever comes next — they all promise.

...

Two reasons.

Order-sensitive equality.

```python
from collections import OrderedDict

{"a": 1, "b": 2} == {"b": 2, "a": 1}                       # True
OrderedDict(a=1, b=2) == OrderedDict(b=2, a=1)             # False
```

Regular dicts compare as equal if they have the same key/value pairs, ignoring order. `OrderedDict` treats order as part of identity. Useful when you're comparing things like JSON parsings where the order has semantic weight (HTTP header lists, signed payloads).

...

Ordered does not mean sorted.

```python
d = {"banana": 1, "apple": 2, "cherry": 3}
list(d)              # ['banana', 'apple', 'cherry'] — insertion order
sorted(d)            # ['apple', 'banana', 'cherry']  — sorted
```

The dict remembers the order you put things in. If you want alphabetical, or by value, or by some custom key, you have to ask for it explicitly:

```python
dict(sorted(d.items()))                        # by key
dict(sorted(d.items(), key=lambda kv: kv[1]))  # by value
```

`sorted` returns a list of tuples; wrap it back in `dict()` to get a sorted dict — which, post-3.7, will stay in that sorted order forever (until you mutate it).

...

Sets are not ordered. `set` and `frozenset` still use the older sparse-table layout, and their iteration order is unspecified:

...

The keys are unique, and the order is preserved.

...

> Dicts have preserved insertion order since CPython 3.6 (as a side effect of the compact-dict memory layout) and since Python 3.7 it's a language guarantee. `OrderedDict` still wins for order-sensitive equality and `move_to_end`. Sets remain unordered.

---

Title: Why is dictionary ordering non-deterministic?
URL: https://stackoverflow.com/questions/14956313/why-is-dictionary-ordering-non-deterministic
Published: N/A
Author: N/A
Highlights:
Update: In Python 3.6, dict has a new implementation which preserves insertion order. From Python 3.7, this order-preserving behaviour is guaranteed:

 the insertion-order preservation nature of dict objects has been declared to be an official part of the Python language spec.

This is the result of a security fix from 2012, which was enabled by default in Python 3.3 (scroll down to "Security improvements").

From the announcement:

 Hash randomization causes the iteration order of dicts and sets to be
 unpredictable and differ across Python runs. Python has never guaranteed
 iteration order of keys in a dict or set, and applications are advised to never
 rely on it. Historically, dict iteration order has not changed very often across
 releases and has always remained consistent between successive executions of
 Python. Thus, some existing applications may be relying on dict or set ordering.
 Because of this and the fact that many Python applications which don't accept
 untrusted input are not vulnerable to this attack, in all stable Python releases
 mentioned here, HASH RANDOMIZATION IS DISABLED BY DEFAULT.

As noted above, the last, capitalized bit is no longer true in Python 3.3.

See also: object.__hash__() documentation ("Note" sidebar).

If absolutely necessary, you can disable hash randomization in versions of Python affected by this behaviour by setting the PYTHONHASHSEED environment variable to 0.

...

Note that Python 3.7 still has non-deterministic sets however. dicts preserve insertion order but sets do not. Sets can exhibit the same random behavior. 

python3 -c "print({str(i) for i in range(9)})"

still gives different results from one run to the next.

---

Title: Does dictionary, json (dumps, loads), defaultdict preserve the order from python 3.7?
URL: https://stackoverflow.com/questions/66878971/does-dictionary-json-dumps-loads-defaultdict-preserve-the-order-from-python
Published: N/A
Author: N/A
Highlights:
Prior to Python 3.7, dict was not guaranteed to be ordered, so inputs
and outputs were typically scrambled unless collections.OrderedDict
was specifically requested. Starting with Python 3.7, the regular dict
became order preserving, so it is no longer necessary to specify
collections.OrderedDict for JSON generation and parsing.

...

Python dicts
Since python 3.7 the implementation of dict is ordered as a part of the specification, not as a side effect of the implementation, so it can be used reliably. OrderedDict is still useful for several reasons:

backward compatibility (if you need to support older python versions)
reorder keys with move_to_end and pop_item
clearer intent: if you rely on you dict keys being ordered, an OrderedDict makes it evident, but you do lose some performance
the order of the keys is considered when comparing OrderedDicts, and ignored for dicts (thanks to @ShadowRanger for the notice):

For example:
from collections import OrderedDict

one_dict = {"a": 1, "b": 2}
another_dict = {"b": 2, "a": 1}

one_ordered_dict = OrderedDict(a=1, b=2)
another_ordered_dict = OrderedDict(b=2, a=1)

print(one_dict == another_dict)
# True
print(one_ordered_dict == another_ordered_dict)
# False

If any of those requirements are needed, OrderedDict can help you, else you can just use a regular dict.
Json dump/load
Regarding the json.dump, this is a different question:
As far as I can tell, the JSONEncoder iterates
over the keys, so it should not change the order.
You can force a lexicographic ordering if you want:
>>> json.dumps({'b': 1, 'a': 2}, sort_keys=True)
'{"a": 2, "b": 1}'

Regarding the loading, I don't see why the order would not be preserved, but I admit I'm getting lost in the source code for the decoder and scanner.
If you want, you can use:
>>> json.loads('{"b": 2, "a": 1}', object_pairs_hook=OrderedDict)
OrderedDict([('b', 2), ('a', 1)])

Nested dicts
The above applies for nested dicts as well: _iterencode_dict is called recursively, and the keys are sorted for all dicts.
Indeed:
>>> json.dumps({'b': 1, 'a': {'d': 1, 'c': 3}}, sort_keys=True)
'{"a": {"c": 3, "d": 1}, "b": 1}'

---

Title: Dictionaries | Scrimba Docs
URL: https://docs.scrimba.com/python/dictionaries
Published: N/A
Author: N/A
Highlights:
A `dict` is a key-value store with average O(1) lookup, insertion, and deletion (O(1) means the cost stays flat no matter how big the dict grows, because keys are found by hashing, turning the key into a number that points straight at its slot). Keys must be hashable, meaning their contents never change so that number stays stable: `str`, `int`, and `tuple` qualify, `list` does not. Values can be any object. Since Python 3.7, dicts keep keys in the order you inserted them, which matters whenever you serialise or display one. The same structure powers a lot of Python under the surface, including the attributes on your own objects, so dicts are worth knowing cold. The Lists chapter covers the position-based cousin.

...

Curly braces with a colon between each key and value, and commas between pairs. Keys are almost always strings. Values can be anything: numbers, strings, other lists, even other dictionaries.

Dict literals use curly braces with `key: value` syntax. Keys can be any immutable (hashable) type: strings, integers, tuples. Values can be any Python object. Dicts preserve insertion order, so when you iterate, you get items in the order they were added.

Dict literals are evaluated left to right. Keys must be hashable (their contents can't change, so the number Python files them under stays put): `str`, `int`, and `tuple` qualify, `list` and `dict` do not. Values have no such restriction. Insertion order is part of the language guarantee as of Python 3.7, so iteration and serialisation are reproducible. One quiet trap: a duplicate key in a single literal does not raise, it keeps the last value and drops the earlier one.

...

Juno Creating a dictionary Keys have to be hashable, so `str`, `int`, and `tuple` are in, `list` and `dict` are out. Insertion order is guaranteed since 3.7, so you can rely on it for output. Watch the duplicate-key literal: it takes the last value silently, no warning.

---

Title: collections.OrderedDict в Python
URL: https://pythonz.net/references/named/collections.ordereddict/
Published: 2021-06-11T04:32:52.000Z
Author: N/A
Highlights:
# collections.OrderedDict

Упорядоченный словарь. Хранит порядок вставки в него элементов.

 OrderedDict([items]) 

Внимание

Начиная с +py3.6 (и официально гарантировано с +py3.7) и обычные словари — dict() — сохраняют порядок вставки элементов.

 Упорядоченные словари походи на обычные, но хранят порядок вставки в них элементов. При итерировании по упорядоченному словарю, его элементы выдаются в том порядке, в каком они были в него добавлены. То есть, даже если значение по ключу обновляется, изначально заданное место ключа в словаре остаётся неизменным. Однако, если удалить ключ и вставить заново, то он очутится на последнем месте.

...

Проверка на равенство одного упорядоченного словаря другому учитывает порядок их элементов: `list(odict1.items())==list(odict2.items())`. В то же время при сравнении с другими представителями отображений порядок во внимание не принимается: это позволяет использовать `OrderedDict` в тех местах, где используются обычные словари.

...

+py3.5 Добавлена поддержка reversed() для элементов (items), ключей (keys), значений (values). +py3.6 После принятия PEP-468, порядок именованных аргументов при вызовах `OrderedDict(z=1, a=2)` и `.update()` тоже учитывается. +py3.8 В соответствии с PEP-584 добавлена поддержка операторов слияния (`|`) и обновления (`|=`).

---

Title: Specify pep-0584 order guarantee
URL: https://github.com/python/peps/pull/1409
Published: N/A
Author: N/A
Highlights:
# Specify pep-0584 order guarantee

- State: merged
- Author: DavidMertz
- Created: 2020-05-19T20:40:19Z
- Updated: 2020-05-20T16:34:00Z
- Repository: python/peps
- Number: #1409
- +2 -0 in 1 files
- Merged: 2020-05-20T16:34:00Z
- Merge commit: 93849f704653eef7651207926446efa6d4d068f4

...

> I agree that a strict reading of the specification section of the PEP probably leaves some questions technically unanswered. Is it typical to update PEP specifications after-the fact, though? I see this more as a historical record and less as a living document.
> 
> The place that really matters, the docs, make ordering semantics clear:
> 
> > Dictionaries preserve insertion order. Note that updating a key does not affect the order.
> 
> But otherwise, none of the documentation goes out of its way to specifically prescribe behavior for pathological cases... even for `dict`, `dict.fromkeys`, or `dict.update`.
> 
> I have no problem updating the PEP if it genuinely disambiguates these specific cases for somebody who has read it and it still confused. It just feels a bit odd to make a change here, of all places.

---

Title: Python Dictionaries
URL: https://www.py4e.com/lectures3/Pythonlearn-09-Dictionaries.pdf
Published: N/A
Author: N/A
Highlights:
## Dictionaries over time in Python

• Prior to Python 3.7 dictionaries did not keep entries in the order of insertion 
• Python 3.7 (2018) and later dictionaries keep entries in the order they were inserted 
• "insertion order" is not "always sorted order"

---

Title: Как использовать OrderedDict, упорядоченный словарь Python. | From-Locals
URL: https://ru.from-locals.com/python-collections-ordereddict/
Published: 2021-11-30T23:37:46.000Z
Author: Zack
Highlights:
Словари Python (объекты типа dict) не сохраняют порядок элементов; CPython делает это с версии 3.6, но это зависит от реализации и неопределенно в других реализациях; спецификация языка сохраняет порядок с версии 3.7.

OrderedDict предоставляется в модуле collections стандартной библиотеки как словарь, сохраняющий порядок. Безопасно использовать именно его.

- OrderedDict — collections — Container datatypes — Python 3.10.0 Documentation

...

До версии 3.5 порядок аргументов ключевых слов не сохранялся, но с версии 3.6 он сохраняется.

> Изменено в версии 3.6: С принятием PEP 468 порядок конструктора OrderedDict и аргументов ключевых слов, передаваемых в метод update(), сохраняется. collections — Container datatypes — Python 3.10.0 Documentation

Обычные словари (объекты типа dict) также могут быть переданы в конструктор, но в случае реализации, где тип dict не сохраняет порядок, сгенерированный из него OrderedDict также не будет сохранять порядок.
=== END OF OUTPUT X14 ===


########## QUESTION q03 ##########
Question: Какое значение по умолчанию у параметра max_connections в PostgreSQL?
Reference answer: 100 (typically; initdb may set less if kernel settings cannot support it).
Reference source: https://www.postgresql.org/docs/current/runtime-config-connection.html

=== OUTPUT B93 ===
Title: max_connections - pgPedia - a PostgreSQL Encyclopedia
URL: https://pgpedia.info/m/max_connections.html
Published: N/A
Author: N/A
Highlights:
A server parameter determining the maximum number of connections

`max_connections` is a configuration parameter determining the maximum number of concurrent connections to the database server.

`max_connections` was added in PostgreSQL 7.1.

## Default value

The default value for `max_connections` is: `100`.

## Usage

On a standby, `max_connections` must be set to the same or higher value as on the primary.

The current value of `max_connections` is one of the GUC parameters recorded in `pg_control`.

---

Title: PostgreSQL Документация: max_connections параметр
URL: https://postgresqlco.nf/doc/ru/param/max_connections/
Published: N/A
Author: N/A
Highlights:
PostgreSQL Документация: max_connections параметр

# max_connections 

| Тип: | `integer` |
| --- | --- |
| По умолчанию: | `100` |
| Минимальный: | `1` |
| Максимальный: | `262143` |
| Контекст: | `postmaster` |
| Перезапуск: | `true` |

 Sets the maximum number of concurrent connections 

Определяет максимальное число одновременных подключений к серверу БД. По умолчанию обычно это 100 подключений, но это число может быть меньше, если ядро накладывает свои ограничения (это определяется в процессе initdb). Этот параметр можно задать только при запуске сервера.

Для ведомого сервера значение этого параметра должно быть больше или равно значению на ведущем. В противном случае на ведомом сервере не будут разрешены запросы.

---

Title: PostgreSQL: Documentation: 18: 19.3. Connections and Authentication
URL: https://www.postgresql.org/docs/current/runtime-config-connection.html
Published: N/A
Author: N/A
Highlights:
While client authentication (Chapter 20) allows fine-grained control over who can access the server, `listen_addresses` controls which interfaces accept connection attempts, which can help prevent repeated malicious connection requests on insecure network interfaces. This parameter can only be set at server start.
`port` (`integer`) #
: The TCP port the server listens on; 5432 by default. Note that the same port number is used for all IP addresses the server listens on. This parameter can only be set at server start.
`max_connections` (`integer`) #
: Determines the maximum number of concurrent connections to the database server. The default is typically 100 connections, but might be less if your kernel settings will not support it (as determined during initdb). This parameter can only be set at server start.

PostgreSQL sizes certain resources based directly on the value of `max_connections`. Increasing its value leads to higher allocation of those resources, including shared memory.

When running a standby server, you must set this parameter to the same or higher value than on the primary server. Otherwise, queries will not be allowed in the standby server.
`reserved_connections` (`integer`) #
: Determines the number of connection “ slots” that are reserved for connections by roles with privileges of the pg_use_reserved_connections role. Whenever the number of free connection slots is greater than superuser_reserved_connections but less than or equal to the sum of `superuser_reserved_connections` and `reserved_connections`, new connections will be accepted only for superusers and roles with privileges of `pg_use_reserved_connections`. If `superuser_reserved_connections` or fewer connection slots are available, new connections will be accepted only for superusers.

---

Title: PostgreSQL Insider - Tuning - Database tuning
URL: https://www.postgresql.fastware.com/postgresql-insider-tun-db-ove
Published: N/A
Author: Fujitsu Australia Ltd
Highlights:
#### Connection parameters

- max_connections - Maximum number of clients that can connect to PostgreSQL at the same time. 

The default value is 100. Higher values increase memory usage and may affect performance. This is because every time you connect to PostgreSQL, a new server process is started, and you need to tune shared memory and semaphores. It is important to set the appropriate number of connections according to the required task.

---

Title: max_connections in Postgres: A Memory Decision in Disguise | myDBA.dev
URL: https://mydba.dev/blog/postgres-max-connections-memory-guide
Published: 2026-08-04T15:17:33.000Z
Author: N/A
Highlights:
`max_connections` defaults to 100 in a stock build. It has `postmaster` context, which means a reload (SIGHUP) does nothing; you need a full server restart.
...
`LEAST({DBInstanceClassMemory/9531392}, 5000)`, is a static parameter in a DB parameter group,

---

Title: PostgreSQL: Documentation: 18: 19.3. Connections and Authentication
URL: https://www.postgresql.org/docs/18/runtime-config-connection.html
Published: 2026-05-14T13:09:46.000Z
Author: N/A
Highlights:
While client authentication (Chapter 20) allows fine-grained control over who can access the server, `listen_addresses` controls which interfaces accept connection attempts, which can help prevent repeated malicious connection requests on insecure network interfaces. This parameter can only be set at server start.
`port` (`integer`) #
: The TCP port the server listens on; 5432 by default. Note that the same port number is used for all IP addresses the server listens on. This parameter can only be set at server start.
`max_connections` (`integer`) #
: Determines the maximum number of concurrent connections to the database server. The default is typically 100 connections, but might be less if your kernel settings will not support it (as determined during initdb). This parameter can only be set at server start.

PostgreSQL sizes certain resources based directly on the value of `max_connections`. Increasing its value leads to higher allocation of those resources, including shared memory.

When running a standby server, you must set this parameter to the same or higher value than on the primary server. Otherwise, queries will not be allowed in the standby server.
`reserved_connections` (`integer`) #
: Determines the number of connection “ slots” that are reserved for connections by roles with privileges of the pg_use_reserved_connections role. Whenever the number of free connection slots is greater than superuser_reserved_connections but less than or equal to the sum of `superuser_reserved_connections` and `reserved_connections`, new connections will be accepted only for superusers and roles with privileges of `pg_use_reserved_connections`. If `superuser_reserved_connections` or fewer connection slots are available, new connections will be accepted only for superusers.

---

Title: 2.1. Process Architecture :: Hironobu SUZUKI @ InterDB
URL: https://www.interdb.jp/pg/pgsql02/01.html
Published: N/A
Author: N/A
Highlights:
process can operate on only one database at a time; therefore, a specific database must
...
PostgreSQL supports concurrent connections from multiple clients, with the maximum number governed by the max_connections configuration parameter (default: 100).

---

Title: Гайд по PostgreSQL для продвинутых разработчиков - UPROGER | Программирование
URL: https://uproger.com/gajd-po-postgresql-dlya-prodvinutyh-razrabotchikov/
Published: 2025-10-10T13:13:47.000Z
Author: N/A
Highlights:
SQL-запросы клиентов. Их число ограничено параметром `max_connections` (по умолчанию 100). Если ... например, PgBouncer) вместо бесконтрольного роста ... количестве подключений каждый backend может получать слишком маленькую долю CPU и памяти.

---

Title: Postgres FATAL: too many connections — как лечить — lenec.ru
URL: https://lenec.ru/p/postgres-fatal-too-many-connections-kak-lechit-439609
Published: 2026-05-24T07:45:08.000Z
Author: N/A
Highlights:
## Что выставлено по умолчанию

Дефолт Postgres — `max_connections = 100`. На managed-хостингах часто чуть выше, но в любом случае это не «бесконечно». Проверить:

```sql
SHOW max_connections;
```

Сколько сейчас открыто и кто открыл — главный запрос для

---

Title: PostgreSQL 配置参数
URL: https://pgsql.cc/wiki/guc/
Published: N/A
Author: N/A
Highlights:
| 参数 | 类型 | 上下文 | 默认值 | 版本变动 7. 4 8. 0 8. 1 8. 2 8. 3 8. 4 9. 0 9. 1 9. 2 9. 3 9. 4 9. 5 9. 6 10 11 12 13 14 15 16 17 18 19 20 | 最近变更 |
| --- | --- | --- | --- | --- | --- |
| File Locations 文件位置 7 个 ↑ | | | | | |
| `config_file` | 字符串 | 重启生效 | `未设置` | | — |
| 指定主服务器配置文件（通常叫 postgresql.conf）。 | | | | | 现存 |
| `data_directory` | 字符串 | 重启生效 | `未设置` | | — |
| 指定用于数据存储的目录。 | | | | | 现存 |
| `extension_destdir` | 字符串 | 会话（超级用户） | `空字符串` | | — |
| 加载扩展时添加到路径前面的目录。 | | | | | 于 18 移除 |
| `external_pid_file` | 字符串 | 重启生效 | `未设置` | | — |
| 指定服务器应创建的额外进程 ID（PID）文件的名称，供服务器管理程序使用。 | | | | | 现存 |
| `hba_file` | 字符串 | 重启生效 | `未设置` | | — |
| 指定基于主机的认证配置文件（通常叫 pg_hba.conf）。 | | | | | 现存 |
| `hosts_file` | 字符串 | | — | | — |
| 指定基于主机的 SSL 配置文件（通常称为 pg_hosts.conf）。 | | | | | 现存 |
| `ident_file` | 字符串 | 重启生效 | `未设置` | | — |
| 指定用于用户名称映射的配置文件（通常叫 pg_ident.conf）。 | | | | | 现存 |
| Connections and Authentication 连接和认证 50 个 ↑ | | | | | |
| 连接设置 11 | | | | | |
| `bonjour` | 布尔 | 重启生效 | `off` | | — |
| 启用通过 Bonjour 通告服务器存在的功能。 | | | | | 现存 |
| `bonjour_name` | 字符串 | 重启生效 | `空字符串` | | — |
| 指定 Bonjour 服务名。 | | | | | 现存 |
| `listen_addresses` | 字符串 | 重启生效 | `localhost` | | — |
| 指定服务器用于监听来自客户端应用程序的连接的 TCP/IP 地址。 | | | | | 现存 |
| `max_connections` | 整数 | 重启生效 | `100` | | 9.6 2 次 |
| 决定数据库服务器允许的最大并发连接数。 | | | | | 现存 |
| `port` | 整数 | 重启生效 | `5432` | | — |
| 服务器监听的 TCP 端口，默认是 5432。 | | | | | 现存 |
| `reserved_connections` | 整数 | 重启生效 | `0` | | — |
| 确定为具有 pg_use_reserved_connections 角色权限的角色保留多少个连接“槽”。 | | | | | 现存 |
| `superuser_reserved_connections` | 整数 | 重启生效 | `3` | | 9.6 2 次 |
| 决定为 PostgreSQL 超级用户连接保留多少个连接“槽”。 | | | | | 现存 |
| `unix_socket_directories` | 字符串 | 重启生效 | `/var/run/postgresql` | | — |
| 指定服务器用于监听来自客户端应用的连接的 Unix 域套接字目录。 | | | | | 现存 |
| `unix_socket_directory` | 字符串 | 重启生效 | `空字符串` | | — |
| 指定服务器用于监听来自客户端应用连接的 Unix 域套接字的目录。 | | | | | 于 9.3 移除 |
| `unix_socket_group` | 字符串 | 重启生效 | `空字符串` | | — |
| 设置 Unix 域套接字的所属组（套接字的所属用户总是启动服务器的用户）。 | | | | | 现存 |
| `unix_socket_permissions` | 整数 | 重启生效 | `511` | | — |
| 设置 Unix 域套接字的访问权限。 | | | | | 现存 |
| TCP 设置 5 | | | | | |
| `client_connection_check_interval` | 整数 | 会话 | `0 ms` | | — |
| 设置查询执行期间可选的客户端连接检查的时间间隔，用于检查客户端是否仍然连接。 | | | | | 现存 |
| `tcp_keepalives_count` | 整数 | 会话 | `0` | | — |
| 指定在服务器与客户端之间的连接被视为中断之前，可以丢失多少个 TCP keepalive 消息。 | | | | | 现存 |
| `tcp_keepalives_idle` | 整数 | 会话 | `0 s` | | — |
| 指定在多久没有网络活动后，操作系统应向客户端发送 TCP keepalive 消息。 | | | | | 现存 |
| `tcp_keepalives_interval` | 整数 | 会话 | `0 s` | | — |
| 指定未被客户端确认收到的 TCP keepalive 消息在多久之后应被重传。 | | | | | 现存 |
| `tcp_user_timeout` | 整数 | 会话 | `0 ms` | | — |
| 指定已发送的数据在 TCP 连接被强制关闭之前最多可以保持未确认状态多长时间。 | | | | | 现存 |
| 认证 10 | | | | | |
| `authentication_timeout` | 整数 | 重载生效 | `1 min` | | — |
| 允许完成客户端认证的最长时间。 | | | | | 现存 |
| `db_user_namespace` | 布尔 | 重载生效 | `off` | | — |
| 此参数启用各数据库独立的用户名。 | | | | | 于 17 移除 |
| `gss_accept_delegation` | 布尔 | 重载生效 | `off` | | — |
| 设置是否接受客户端的 GSSAPI 委派。 | | | | | 现存 |
| `krb_caseins_users` | 布尔 | 重载生效 | `off` | | — |
| 设置是否应该以大小写不敏感的方式对待 GSSAPI 用户名。 | | | | | 现存 |
| `krb_server_keyfile` | 字符串 | 重载生效 | `FILE:/etc/postgresql-common/krb5.keytab` | | 9.1 1 次 |
| 设置服务器的 Kerberos 密钥文件的位置。 | | | | | 现存 |
| `md5_password_warnings` | 布尔 | 会话 | `on` | | — |
| 控制在使用 MD5 加密密码成功认证时，或者在 CREATE ROLE 或 ALTER ROLE 语句设置 MD5 加密密码时，是否生成有关 MD5 密码已弃用的 WARNING。 | | | | | 现存 |
| `oauth_validator_libraries` | 字符串 | 重载生效 | `空字符串` | | — |
| 设置用于验证 OAuth 连接令牌的库。 | | | | | 现存 |
| `password_encryption` | 枚举 | 会话 | `scram-sha-256` | | 14 2 次 |
| 当在 CREATE ROLE 或 ALTER ROLE 中指定密码时，该参数决定用于加密密码的算法。 | | | | | 现存 |
| `password_expiration_warning_threshold` | 整数 | | — | | — |
| 当此参数大于零时，如果距离已认证角色的密码过期剩余时间少于这个时长，服务器会在成功完成密码认证后发出 WARNING。 | | | | | 现存 |
| `scram_iterations` | 整数 | 会话 | `4096` | | — |
| 使用 SCRAM-SHA-256 加密密码时执行的计算迭代次数。 | | | | | 现存 |
| 安全和认证 2 | | | | | |
| `krb_srvname` | 字符串 | 重载生效 | `postgres` | | — |
| 设置 Kerberos 服务名。 | | | | | 于 9.4 移除 |
| `ssl_renegotiation_limit` | 整数 | 会话 | `0 B` | | — |
| 指定在一个SSL加密连接上可以流过多少数据之后将进行会话密钥的重新协商。 | | | | | 于 9.5 移除 |
| SSL 17 | | | | | |
| `ssl` | 布尔 | 重载生效 | `off` | | 10 1 次 |
| 启用 SSL 连接。 | | | | | 现存 |
| `ssl_ca_file` | 字符串 | 重载生效 | `空字符串` | | 10 1 次 |
| 指定包含 SSL 服务器证书颁发机构（CA）的文件名。 | | | | | 现存 |
| `ssl_cert_file` | 字符串 | 重载生效 | `server.crt` | | 10 1 次 |
| 指定包含 SSL 服务器证书的文件名。 | | | | | 现存 |
| `ssl_ciphers` | 字符串 | 重载生效 | `HIGH:MEDIUM:+3DES:!aNULL` | | 10 3 次 |
| 指定允许用于 TLS 1.2 及更低版本连接的 SSL 密码套件列表；对于 TLS 1.3 连接，请参见 ssl_tls13_ciphers。 | | | | | 现存 |
| `ssl_crl_dir` | 字符串 | 重载生效 | `空字符串` | | — |
| 指定包含 SSL 客户端证书吊销列表（CRL）的目录名称。 | | | | | 现存 |
| `ssl_crl_file` | 字符串 | 重载生效 | `空字符串` | | 10 1 次 |
| 指定包含 SSL 客户端证书吊销列表（CRL）的文件名。 | | | | | 现存 |
| `ssl_dh_params_file` | 字符串 | 重载生效 | `空字符串` | | — |
| 指定包含 Diffie-Hellman 参数的文件名，这些参数用于所谓临时 DH 系列的 SSL 密码套件。 | | | | | 现存 |
| `ssl_ecdh_curve` | 字符串 | 重载生效 | `prime256v1` | | 10 1 次 |
| 指定在 ECDH 密钥交换中使用的曲线名称。 | | | | | 于 18 移除 |
| `ssl_groups` | 字符串 | 重载生效 | `X25519:prime256v1` | | — |
| 指定用于 TLS 密钥交换的命名组。 | | | | | 现存 |
| `ssl_key_file` | 字符串 | 重载生效 | `server.key` | | 10 1 次 |
| 指定包含 SSL 服务器私钥的文件名。 | | | | | 现存 |
| `ssl_max_protocol_version` | 枚举 | 重载生效 | `空字符串` | | — |
| 设置要使用的最高 SSL/TLS 协议版本。 | | | | | 现存 |
| `ssl_min_protocol_version` | 枚举 | 重载生效 | `TLSv1.2` | | 13 1 次 |
| 设置要使用的最低 SSL/TLS 协议版本。 | | | | | 现存 |
| `ssl_passphrase_command` | 字符串 | 重载生效 | `空字符串` | | — |
| 设置获取用于解密私钥等 SSL 文件的口令时要调用的外部命令。 | | | | | 现存 |
| `ssl_passphrase_command_supports_reload` | 布尔 | 重载生效 | `off` | | — |
| 此参数决定：配置重载期间，如果密钥文件需要口令，是否也调用 ssl_passphrase_command 设置的口令命令。 | | | | | 现存 |
| `ssl_prefer_server_ciphers` | 布尔 | 重载生效 | `on` | | 10 1 次 |
| 指定是否使用服务器的 SSL 密码套件优先顺序，而非客户端的优先顺序。 | | | | | 现存 |
| `ssl_sni` | 布尔 | | — | | — |
| 启用 SSL 连接的 SNI 配置。 | | | | | 现存 |
| `ssl_tls13_ciphers` | 字符串 | 重载生效 | `空字符串` | | — |
| 指定允许用于 TLS 版本 1.3 连接的密码套件列表。 | | | | | 现存 |
| Connections and Authentication 5 | | | | | |
| `krb_realm` | 字符串 | | — | | — |
| 设置对 Kerberos、GSSAPI 和 SSPI 用户名进行匹配时所用的 realm。 | | | | | 于 8.4 移除 |
| `krb_server_hostname` | 字符串 | | — | | — |
| 设置服务主体的主机名部分。 | | | | | 于 8.4 移除 |
| `rendezvous_name` | 字符串 | | — | | — |
| 指定Rendezvous广播名称。 | | | | | 于 8.1 移除 |
| `tcpip_socket` | 布尔 | | — | | — |
| 如果为真，服务器将接受 TCP/IP 连接。 | | | | | 于 8.0 移除 |
| `virtual_host` | 字符串 | | — | | — |
| 指定服务器用于监听来自客户端应用连接的主机名或 IP 地址。 | | | | | 于 8.0 移除 |
| Resource Usage 资源消耗 61 个 ↑ | | | | | |
| 内存 23 | | | | | |
| `autovacuum_work_mem` | 整数 | 重载生效 | `-1 kB` | | — |
| 指定每个自动清理工作进程可使用的最大内存量。 | | | | | 现存 |
| `commit_timestamp_buffers` | 整数 | 重启生效 | `0 B (0 × 8kB)` | | — |
| 指定用于缓存 pg_commit_ts 内容的内存量（参见表 66.1）。 | | | | | 现存 |
| `dynamic_shared_memory_type` | 枚举 | 重启生效 | `posix` | | 12 1 次 |
| 指定服务器应使用的动态共享内存实现。 | | | | | 现存 |
| `hash_mem_multiplier` | 浮点 | 会话 | `2` | | 15 1 次 |
| 用于计算基于 hash 的操作可以使用的最大内存量。 | | | | | 现存 |
| `huge_page_size` | 整数 | 重启生效 | `0 B` | | — |
| 控制通过 huge_pages 启用巨型页时所使用的页大小。 | | | | | 现存 |
| `huge_pages` | 枚举 | 重启生效 | `try` | | — |
| 控制是否为主共享内存区域请求巨型页。 | | | | | 现存 |
| `logical_decoding_work_mem` | 整数 | 会话 | `64 MiB` | | — |
| 指定逻辑解码在将部分已解码的更改写入本地磁盘之前可使用的最大内存量。 | | | | | 现存 |
| `maintenance_work_mem` | 整数 | 会话 | `64 MiB` | | 17 2 次 |
| 指定维护操作（如 VACUUM、CREATE INDEX 和 ALTER TABLE ADD FOREIGN KEY）可使用的最大内存量。 | | | | | 现存 |
| `max_prepared_transactions` | 整数 | 重启生效 | `0` | | 9.6 2 次 |
| 设置可同时处于“预备”状态的事务的最大数量（见 PREPARE TRANSACTION）。 | | | | | 现存 |
| `max_stack_depth` | 整数 | 会话（超级用户） | `100 KiB` | | — |
| 指定服务器执行栈的最大安全深度。
=== END OF OUTPUT B93 ===

=== OUTPUT A22 ===
Значение по умолчанию для `max_connections` в PostgreSQL — **100**. Это подтверждает справочник по параметрам, где указано Default: 100, а также документация-зеркало, согласно которой значение обычно равно 100, но может быть меньше, если ядро системы не поддерживает его при инициализации (initdb).

Один источник называет другое число: Command Prompt пишет о лимите в 115 соединений, из которых 15 зарезервированы для суперпользователей. Это расходится с остальными источниками. Другие материалы указывают, что по умолчанию зарезервировано 3 слота (параметр `superuser_reserved_connections`), то есть из 100 обычным пользователям доступно 97. Поэтому ориентироваться стоит на 100.

Sources:
1. https://help.puppet.com/pe/current/topics/postgresql-max-connections.htm
2. https://commandprompt.com/education/how-to-increase-maximum-connections-in-postgresql
3. https://m.novel.qq.com/read/1036701358/28
4. https://help.arcgis.com/en/arcgisdesktop/10.0/help/002p/002p00000003000000.htm
5. https://resources.arcgis.com/en/help/main/10.1/002p/002p00000003000000.htm
6. https://postgresqlco.nf/en/doc/param/max_connections
7. https://postgresqlco.nf/doc/en/param/max_connections/
=== END OF OUTPUT A22 ===

=== OUTPUT K74 ===
По умолчанию значение параметра `max_connections` в PostgreSQL равно **100**. [1]

Несколько важных деталей об этом параметре:

-   **Доступные слоты для обычных пользователей:** Из 100 подключений по умолчанию 3 зарезервированы для суперпользователей (параметр `superuser_reserved_connections`), поэтому обычным ролям доступно 97 одновременных сессий. [2]
    
-   **Ограничения при инициализации:** При создании кластера через `initdb` значение может быть автоматически снижено, если операционная система или ядро накладывают более жесткие лимиты на ресурсы. [1]
    
-   **Диапазон значений:** Параметр принимает целые числа от `1` до `262 143`. [2]
    
-   **Применение изменений:** Настройка задается в файле `postgresql.conf` и вступает в силу только после полной перезагрузки сервера БД. Подробнее об этом параметре можно прочитать в документации PostgreSQL. [3]
    

Если вы планируете увеличить этот лимит под высокую нагрузку, я могу помочь рассчитать оптимальное значение под вашу **оперативную память** или подобрать настройки для **пула соединений** (например, PgBouncer). Подсказать, как это лучше сделать?

Sources:
1. https://postgresqlco.nf/doc/ru/param/max_connections/
2. https://sql-ex.ru/blogs/?/Vsjo_o_GUC_po_porJadku_max_connections.html
3. https://help.pilotems.com/ru/Content/PG_nastroyka_bd.htm?TocPath=%D0%A3%D1%81%D1%82%D0%B0%D0%BD%D0%BE%D0%B2%D0%BA%D0%B0%2C%20%D0%BD%D0%B0%D1%81%D1%82%D1%80%D0%BE%D0%B9%D0%BA%D0%B0%2C%20%D0%BE%D0%B1%D0%BD%D0%BE%D0%B2%D0%BB%D0%B5%D0%BD%D0%B8%D0%B5|%D0%A0%D0%B0%D0%B1%D0%BE%D1%82%D0%B0%20%D1%81%20%D0%B1%D0%B0%D0%B7%D0%B0%D0%BC%D0%B8%20%D0%B4%D0%B0%D0%BD%D0%BD%D1%8B%D1%85|_____2
=== END OF OUTPUT K74 ===


########## QUESTION q04 ##########
Question: In which Rust release did the 2021 edition become stable?
Reference answer: Rust 1.56.0 (October 21, 2021).
Reference source: https://doc.rust-lang.org/edition-guide/rust-2021/index.html

=== OUTPUT T14 ===
Title: Announcing Rust 1.56.0 and Rust 2021 | Rust Blog
URL: https://blog.rust-lang.org/2021/10/21/Rust-1.56.0/
Published: 2021-10-21T00:00:00.000Z
Author: The Rust Release Team
Highlights:
## Announcing Rust 1.56.0 and Rust 2021

Oct. 21, 2021 · The Rust Release Team 

The Rust team is happy to announce a new version of Rust, 1.56.0. This stabilizes the 2021 edition as well. Rust is a programming language empowering everyone to build reliable and efficient software.

If you have a previous version of Rust installed via rustup, getting Rust 1.56.0 is as easy as:

```
$ rustup update stable
```

...

We wrote about plans for the Rust 2021 Edition in May.

---

Title: Rust 2021 Edition is Here: Q&A with Armin Ronacher - InfoQ
URL: https://www.infoq.com/news/2021/10/rust-2021-edition-qa/
Published: 2021-10-22T14:00:00.000Z
Author: Sergio De Simone
Highlights:
- Sergio De Simone 

Rust 2021 Edition hit the road perfectly on schedule on October 21, along with Rust 1.56.0. The latest version of the language includes support for disjoint capture, `or` patterns in macro rules, and more.

---

Title: Rust 2021 - The Rust Edition Guide
URL: https://doc.rust-lang.org/stable/edition-guide/rust-2021/
Published: N/A
Author: N/A
Highlights:
# Rust 2021

| Info | |
| --- | --- |
| RFC | #3085 |
| Release version | 1.56.0 |

The Rust 2021 Edition contains several changes that bring new capabilities and more consistency to the language, and opens up room for expansion in the future. The

---

Title: How to fix "this version of Cargo is older than the `2021` edition" error?
URL: https://stackoverflow.com/questions/74697023/how-to-fix-this-version-of-cargo-is-older-than-the-2021-edition-error
Published: N/A
Author: N/A
Highlights:
Your problem is not a platform difference; you simply have an old version. The 2021 language edition was added with Rust release version 1.56.0, in October 2021. You need to install a Rust version that is at least that new.
The recommended way to install and maintain a Rust toolchain is with Rustup. I can personally confirm that it will work on ARM Chromebook Linux.

---

Title: Diff - refs/tags/1.56.0^1..refs/tags/1.56.0 - third_party/rust - Git at Google
URL: https://fuchsia.googlesource.com/third_party/rust/+/refs/tags/1.56.0%5E1..refs/tags/1.56.0/
Published: N/A
Author: N/A
Highlights:
```
Auto merge of #90004 - pietroalbini:stable-next, r=pietroalbini

Rust 1.56.0 stable release

This PR bumps 1.56.0 to the stable channel. This also includes a backport for:

* Latest changes to the release notes
* #89867

...

```
@@ -1,3 +1,185 @@
+Version 1.56.0 (2021-10-21)
+========================
+
+Language
+--------
+
+- [The 2021 Edition is now stable.][rust#88100]
+  See [the edition guide][rust-2021-edition-guide] for more details.
+- [The pattern in `binding @ pattern` can now also introduce new bindings.][rust#85305]
+- [Union field access is permitted in `const fn`.][rust#85769]
+
+[rust-2021-edition-guide]: https://doc.rust-lang.org/nightly/edition-guide/rust-2021/index.html
+
+Compiler
+--------
+
+- [Upgrade to LLVM 13.][rust#87570]
+- [Support memory, address, and thread sanitizers on aarch64-unknown-freebsd.][rust#88023]
+- [Allow specifying a deployment target version for all iOS targets][rust#87699]
+- [Warnings can be forced on with `--force-warn`.][rust#87472]
+  This feature is primarily intended for usage by `cargo fix`, rather than end users.
+- [Promote `aarch64-apple-ios-sim` to Tier 2\*.][rust#87760]
+- [Add `powerpc-unknown-freebsd` at Tier 3\*.][rust#87370]
+- [Add `riscv32imc-esp-espidf` at Tier 3\*.][rust#87666]
+
+\* Refer to Rust's [platform support page][platform-support-doc] for more
+information on Rust's tiered platform support.
+
+Libraries
+---------
+
+- [Allow writing of incomplete UTF-8 sequences via stdout/stderr on Windows.][rust#83342]
+  The Windows console still requires valid Unicode, but this change allows
+  splitting a UTF-8 character across multiple write calls. This allows, for
+  instance, programs that just read and write data buffers (e.g. copying a file
+  to stdout) without regard for Unicode or character boundaries.
+- [Prefer `AtomicU{64,128}` over Mutex for Instant backsliding protection.][rust#83093]
+  For this use case, atomics scale much better under contention.
+- [Implement `Extend<(A, B)>` for `(Extend<A>, Extend<B>)`][rust#85835]
+- [impl Default, Copy, Clone for std::io::Sink and std::io::Empty][rust#86744]
+- [`impl From<[(K, V); N]>` for all collections.][rust#84111]
+- [Remove `P: Unpin` bound on impl Future for Pin.][rust#81363]
+- [Treat invalid environment variable names as non-existent.][rust#86183]
+  Previously, the environment functions would panic if given a variable name
+  with an internal null character or equal sign (`=`). Now, these functions will
+  just treat such names as non-existent variables, since the OS cannot represent
+  the existence of a variable with such a name.
+
+Stabilised APIs
+---------------
+
+- [`std::os::unix::fs::chroot`]
+- [`UnsafeCell::raw_get`]
+- [`BufWriter::into_parts`]
+- [`core::panic::{UnwindSafe, RefUnwindSafe, AssertUnwindSafe}`]
+  These APIs were previously stable in `std`, but are now also available in `core`.
+- [`Vec::shrink_to`]
+- [`String::shrink_to`]
+- [`OsString::shrink_to`]
+- [`PathBuf::shrink_to`]
+- [`BinaryHeap::shrink_to`]
+- [`VecDeque::shrink_to`]
+- [`HashMap::shrink_to`]
+- [`HashSet::shrink_to`]
+
+These APIs are now usable in const contexts:
+
+- [`std::mem::transmute`]
+- [`[T]::first`][`slice::first`]
+- [`[T]::split_first`][`slice::split_first`]
+- [`[T]::last`][`slice::last`]
+- [`[T]::split_last`][`slice::split_last`]
+
+Cargo
+-----
+
+- [Cargo supports specifying a minimum supported Rust version in Cargo.toml.][`rust-version`]
+  This has no effect at present on dependency version selection.
+  We encourage crates to specify their minimum supported Rust version, and we encourage CI systems
+  that support Rust code to include a crate's specified minimum version in the text matrix for that
+  crate by default.
+
+Compatibility notes
+-------------------
+
+- [Update to new argument parsing rules on Windows.][rust#87580]
+  This adjusts Rust's standard library to match the behavior of the standard
+  libraries for C/C++. The rules have changed slightly over time, and this PR
+  brings us to the latest set of rules (changed in 2008).
+- [Disallow the aapcs calling convention on aarch64][rust#88399]
+  This was already not supported by LLVM; this change surfaces this lack of
+  support with a better error message.
+- [Make `SEMICOLON_IN_EXPRESSIONS_FROM_MACROS` warn by default][rust#87385]
+- [Warn when an escaped newline skips multiple lines.][rust#87671]
+- [Calls to `libc::getpid` / `std::process::id` from `Command::pre_exec`
+   may return different values on glibc <= 2.24.][rust#81825]
+   Rust now invokes the `clone3` system call directly, when available, to use new functionality
+   available via that system call. Older versions of glibc cache the result of `getpid`, and only
+   update that cache when calling glibc's clone/fork functions, so a direct system call bypasses
+   that cache update. glibc 2.25 and newer no longer cache `getpid` for exactly this reason.
+
+Internal changes
+----------------
+These changes provide no direct user facing benefits, but represent significant
+improvements to the internals and overall performance of rustc
+and related tools.
+
+- [LLVM is compiled with PGO in published x86_64-unknown-linux-gnu artifacts.][rust#88069]
+  This improves the performance of most Rust builds.
+- [Unify representation of macros in internal data structures.][rust#88019]
+  This change fixes a host of bugs with the handling of macros by the compiler,
+  as well as rustdoc.
+
+[`std::os::unix::fs::chroot`]: https://doc.rust-lang.org/stable/std/os/unix/fs/fn.chroot.html
+[`Iterator::intersperse`]: https://doc.rust-lang.org/stable/std/iter/trait.Iterator.html#method.intersperse
+[`Iterator::intersperse_with`]: https://doc.rust-lang.org/stable/std/iter/trait.Iterator.html#method.intersperse
+[`UnsafeCell::raw_get`]: https://doc.rust-lang.org/stable/std/cell/struct.UnsafeCell.html#method.raw_get
+[`BufWriter::into_parts`]: https://doc.rust-lang.org/stable/std/io/struct.BufWriter.html#method.into_parts
+[`core::panic::{UnwindSafe, RefUnwindSafe, AssertUnwindSafe}`]: https://github.com/rust-lang/rust/pull/84662
+[`Vec::shrink_to`]: https://doc.rust-lang.org/stable/std/vec/struct.Vec.html#method.shrink_to
+[`String::shrink_to`]: https://doc.rust-lang.org/stable/std/string/struct.String.html#method.shrink_to
+[`OsString::shrink_to`]: https://doc.rust-lang.org/stable/std/ffi/struct.OsString.html#method.shrink_to
+[`PathBuf::shrink_to`]: https://doc.rust-lang.org/stable/std/path/struct.PathBuf.html#method.shrink_to
+[`BinaryHeap::shrink_to`]: https://doc.rust-lang.org/stable/std/collections/struct.BinaryHeap.html#method.shrink_to
+[`VecDeque::shrink_to`]: https://doc.rust-lang.org/stable/std/collections/struct.VecDeque.html#method.shrink_to
+[`HashMap::shrink_to`]: https://doc.rust-lang.org/stable/std/collections/hash_map/struct.HashMap.html#method.shrink_to
+[`HashSet::shrink_to`]: https://doc.rust-lang.org/stable/std/collections/hash_set/struct.HashSet.html#method.shrink_to
+[`std::mem::transmute`]: https://doc.rust-lang.org/stable/std/mem/fn.transmute.html
+[`slice::first`]: https://doc.rust-lang.org/stable/std/primitive.slice.html#method.first
+[`slice::split_first`]: https://doc.rust-lang.org/stable/std/primitive.slice.html#method.split_first
+[`slice::last`]: https://doc.rust-lang.org/stable/std/primitive.slice.html#method.last
+[`slice::split_last`]: https://doc.rust-lang.org/stable/std/primitive.slice.html#method.split_last
+[`rust-version`]: https://doc.rust-lang.org/nightly/cargo/reference/manifest.html#the-rust-version-field
+[rust#87671]: https://github.com/rust-lang/rust/pull/87671
+[rust#86183]: https://github.com/rust-lang/rust/pull/86183
+[rust#87385]: https://github.com/rust-lang/rust/pull/87385
+[rust#88100]: https://github.com/rust-lang/rust/pull/88100
+[rust#86860]: https://github.com/rust-lang/rust/pull/86860
+[rust#84039]: https://github.com/rust-lang/rust/pull/84039
+[rust#86492]: https://github.com/rust-lang/rust/pull/86492
+[rust#88363]: https://github.com/rust-lang/rust/pull/88363
+[rust#85305]: https://github.com/rust-lang/rust/pull/85305
+[rust#87832]: https://github.com/rust-lang/rust/pull/87832
+[rust#88069]: https://github.com/rust-lang/rust/pull/88069
+[rust#87472]: https://github.com/rust-lang/rust/pull/87472
+[rust#87699]: https://github.com/rust-lang/rust/pull/87699
+[rust#87570]: https://github.com/rust-lang/rust/pull/87570
+[rust#88023]: https://github.com/rust-lang/rust/pull/88023
+[rust#87760]: https://github.com/rust-lang/rust/pull/87760
+[rust#87370]: https://github.com/rust-lang/rust/pull/87370
+[rust#87580]: https://github.com/rust-lang/rust/pull/87580
+[rust#83342]: https://github.com/rust-lang/rust/pull/83342
+[rust#83093]: https://github.com/rust-lang/rust/pull/83093
+[rust#88177]: https://github.com/rust-lang/rust/pull/88177
+[rust#88548]: https://github.com/rust-lang/rust/pull/88548
+[rust#88551]: https://github.com/rust-lang/rust/pull/88551
+[rust#88299]: https://github.com/rust-lang/rust/pull/88299
+[rust#88220]: https://github.com/rust-lang/rust/pull/88220
+[rust#85835]: https://github.com/rust-lang/rust/pull/85835
+[rust#86879]: https://github.com/rust-lang/rust/pull/86879
+[rust#86744]: https://github.com/rust-lang/rust/pull/86744
+[rust#84662]: https://github.com/rust-lang/rust/pull/84662
+[rust#86593]: https://github.com/rust-lang/rust/pull/86593
+[rust#81050]: https://github.com/rust-lang/rust/pull/81050
+[rust#81363]: https://github.com/rust-lang/rust/pull/81363
+[rust#84111]: https://github.com/rust-lang/rust/pull/84111
+[rust#85769]: https://github.com/rust-lang/rust/pull/85769#issuecomment-854363720
+[rust#88490]: https://github.com/rust-lang/rust/pull/88490
+[rust#88269]: https://github.com/rust-lang/rust/pull/88269
+[rust#84176]: https://github.com/rust-lang/rust/pull/84176
+[rust#88399]: https://github.com/rust-lang/rust/pull/88399
+[rust#88227]: https://github.com/rust-lang/rust/pull/88227
+[rust#88200]: https://github.com/rust-lang/rust/pull/88200
+[rust#82776]: https://github.com/rust-lang/rust/pull/82776
+[rust#88077]: https://github.com/rust-lang/rust/pull/88077
+[rust#87728]: https://github.com/rust-lang/rust/pull/87728
+[rust#87050]: https://github.com/rust-lang/rust/pull/87050
+[rust#87619]: https://github.com/rust-lang/rust/pull/87619
+[rust#81825]: https://github.com/rust-lang/rust/pull/81825#issuecomment-808406918
+[rust#88019]: https://github.com/rust-lang/rust/pull/88019
+[rust#87666]: https://github.com/rust-lang/rust/pull/87666
+
 Version 1.55.0 (2021-09-09)
 ============================

---

Title: Rust 2021 - The Rust Edition Guide
URL: https://doc.rust-lang.org/edition-guide/rust-2021/index.html
Published: N/A
Author: N/A
Highlights:
# Rust 2021

| Info | |
| --- | --- |
| RFC | #3085 |
| Release version | 1.56.0 |

The Rust 2021 Edition contains several changes that bring new capabilities and more consistency to the language, and opens up room for expansion in the future. The

---

Title: The Plan for the Rust 2021 Edition | Rust Blog
URL: https://blog.rust-lang.org/2021/05/11/edition-2021/
Published: 2021-05-11T00:00:00.000Z
Author: N/A
Highlights:
## What comes next?

Our plan is to have these changes merged and fully tested by September, to make sure the 2021 edition makes it into Rust 1.56.0. Rust 1.56.0 will then be in beta for six weeks, after which it is released as stable on October 21st.

---

Title: 🎉 Rust 2021 celebration and thanks
URL: https://github.com/rust-lang/rust/issues/88623
Published: N/A
Author: N/A
Highlights:
**The beta version of Rust 1.56 is about to branch off, which includes a *stable `rustc --edition=2021`*!** 
 
This means that, other than backports, all new development goes into 1.57, and the first version with a stable Rust 2021 is very likely going to be Rust 1.56 which will ship in a bit more than six weeks from now, on october 21st!

---

Title: Stabilize Rust 2021
URL: https://github.com/rust-lang/rust/issues/87959
Published: N/A
Author: N/A
Highlights:
- [x] FCP on closure capture changes: https://github.com/rust-lang/rust/issues/88126 
- [x] FCP on reserved prefixes: https://github.com/rust-lang/rust/issues/88140 
- [x] FCP on force-warn: https://github.com/rust-lang/rust/issues/86516#issuecomment-900382193 
- [x] Decide that Rust 1.56 will ship Rust 2021 as stable: Zulip thread 
- [x] Make `--edition=2021` stable in rustc: https://github.com/rust-lang/rust/pull/88100 
- [x] Remove/stabilize experimental 2021 cargo feature: https://github.com/rust-lang/cargo/pull/9800 
 - [x] Update `cargo` submodule: https://github.com/rust-lang/rust/pull/88563 
- [x] Update edition guide and other documentation to reflect stability. 
 - [x] Edition guide: https://github.com/rust-lang/edition-guide/pull/266 
 - [x] Update edition-guide submodule: https://github.com/rust-lang/rust/pull/88563 
 - [x] Check if there's any other documentation that needs updating

---

Title: Rust 2021 public testing period | Rust Blog
URL: https://blog.rust-lang.org/2021/07/21/Rust-2021-public-testing/
Published: 2021-07-21T00:00:00.000Z
Author: N/A
Highlights:
We are happy to announce that the Rust 2021 edition is entering its public testing period. All of the planned features for the edition are now available on nightly builds along with migrations that should move your code from Rust 2018 to Rust 2021.

...

Note that Rust 2021 is still unstable, so you can expect bugs and other changes! We recommend migrating your crates in a temporary copy of your code versus your main branch. If you do encounter problems, or find areas where quality could be improved (missing documentation, confusing error messages, etc) please file an issue and tell us about it! Thank you!

### What comes next

We are targeting stabilization of all Rust 2021 for Rust 1.56, which will be released on October 21st, 2021. Per the Rust train release model, that means all features and work must be landed on nightly by September 7th.
=== END OF OUTPUT T14 ===

=== OUTPUT V59 ===
The 2021 edition became stable with **Rust 1.56.0**, released on October 21, 2021. One SD Times article reports that the Rust 2021 edition and Rust 1.56.0 stable are now available for download. The Rust blog's July 2021 public testing announcement had already targeted stabilization of all Rust 2021 for Rust 1.56, which will be released on October 21st, 2021.

Sources:
1. https://sdtimes.com/?p=45616
2. https://sdtimes.com/softwaredev/rust-2021-includes-several-quality-of-life-improvements/
3. https://sdtimes.com/?p=44001
4. https://blog.rust-lang.org/2021/07/21/Rust-2021-public-testing/
5. https://www.techzine.eu/news/devops/63438/the-latest-version-of-the-programming-language-rust-is-now-available/
6. https://blog.rust-lang.org/2021/05/11/edition-2021/
7. https://sdtimes.com/softwaredev/what-to-expect-in-rust-2021/
=== END OF OUTPUT V59 ===

=== OUTPUT K19 ===
The Rust 2021 edition became stable in **Rust 1.56.0**. [1]

According to the official [Rust Blog announcement](https://blog.rust-lang.org/2021/10/21/Rust-1.56.0/):

-   **Release Date:** October 21, 2021.
    
-   **Edition Significance:** Rust 2021 was the third major edition of the language, introducing quality-of-life ergonomics and Cargo improvements while keeping backward compatibility optional via crate settings. [2]
    

If you are working with older crates or planning a migration, I can break down the **key breaking changes** introduced in Rust 2021 or show how to **upgrade a project** to a newer edition. Would that help?

Sources:
1. https://blog.rust-lang.org/2021/10/21/Rust-1.56.0/
2. https://www.devclass.com/development/2021/10/27/rust-1560-arrives-delivering-rust-2021-edition-support/1624005
3. https://www.facebook.com/fb-answers/rust-1-56-stable-edition-2021-release-notes/
=== END OF OUTPUT K19 ===


########## QUESTION q05 ##########
Question: Какой HTTP-код означает «Misdirected Request» и в каком RFC он сейчас определён?
Reference answer: 421; defined in RFC 9110 (HTTP Semantics).
Reference source: https://www.rfc-editor.org/rfc/rfc9110

=== OUTPUT G44 ===
**Статус «Misdirected Request» соответствует HTTP-коду 421, который сейчас определён в спецификации** **[RFC 9110](https://httpwg.org/specs/rfc9110.html) (раздел 15.5.20)**. [1]

Этот код ошибки клиента (`4xx`) означает, что запрос был направлен на сервер, который не может или не готов сформировать авторитетный ответ для указанной комбинации схемы (например, `https`) и хоста (authority) в целевом URI. Ранее код 421 был описан в устаревшем RFC 7540 (HTTP/2), но с публикацией [RFC 9110 (HTTP Semantics)](https://www.protokols.ru/rfc9110/) он перенесён в общую семантику протокола HTTP. [2]

**Основные особенности и причины возникновения:**

-   **Повторное использование соединений (HTTP/2):** Клиент может переиспользовать открытое соединение для другого домена, если тот покрывается тем же TLS-сертификатом, но целевой сервер не настроен на обслуживание этого хоста. [3]
    
-   **Несовпадение SNI и заголовка `Host`:** Ошибка часто возникает в веб-серверах (например, Apache или Nginx), когда имя хоста в TLS-рукопожатии (SNI) не совпадает с заголовком `Host` в самом HTTP-запросе. [4]
    
-   **Поведение клиента:** Согласно [документации MDN](https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Status/421), получив ответ `421`, клиент может автоматически повторить запрос через новое, отдельное соединение независимо от идемпотентности метода. [2]
    

Если вы столкнулись с ошибкой **421 Misdirected Request** на практике, я могу подсказать, как исправить конфигурацию **SNI или виртуальных хостов** для вашего веб-сервера (Nginx, Apache, Cloudflare). Какой сервер или прокси вы используете?

Sources:
1. https://httpwg.org/specs/rfc9110.html
2. https://www.protokols.ru/rfc9110/
3. https://www.statproxies.com/glossary/http-status-codes/421
4. https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Status/421
5. https://securitylab.pro/blog/sni-error/
=== END OF OUTPUT G44 ===

=== OUTPUT X48 ===
Title: Hypertext Transfer Protocol (HTTP) Status Code Registry
URL: https://www.iana.org/assignments/http-status-codes
Published: N/A
Author: N/A
Highlights:
### Registration Procedure(s)

- IETF Review

- RFC 9110, Section 16.2.1: HTTP Semantics

...

```
1xx: Informational - Request received, continuing process
2xx: Success - The action was successfully received, understood, and accepted
3xx: Redirection - Further action must be taken in order to complete the request
4xx: Client Error - The request contains bad syntax or cannot be fulfilled
5xx: Server Error - The server failed to fulfill an apparently valid request
```

...

| Value | Description | Reference |
| --- | --- | --- |
| 100 | Continue | RFC 9110, Section 15.2.1 |
| 101 | Switching Protocols | RFC 9110, Section 15.2.2 |
| 102 | Processing | RFC 2518 |
| 103 | Early Hints | RFC 8297 |
| 104 | Upload Resumption Supported (TEMPORARY - registered 2024-11-13, extension registered 2025-09-15, expires 2026-11-13) | draft-ietf-httpbis-resumable-upload-05 |
| 105-199 | Unassigned | |
| 200 | OK | RFC 9110, Section 15.3.1 |
| 201 | Created | RFC 9110, Section 15.3.2 |
| 202 | Accepted | RFC 9110, Section 15.3.3 |
| 203 | Non-Authoritative Information | RFC 9110, Section 15.3.4 |
| 204 | No Content | RFC 9110, Section 15.3.5 |
| 205 | Reset Content | RFC 9110, Section 15.3.6 |
| 206 | Partial Content | RFC 9110, Section 15.3.7 |
| 207 | Multi-Status | RFC 4918 |
| 208 | Already Reported | RFC 5842 |
| 209-225 | Unassigned | |
| 226 | IM Used | RFC 3229 |
| 227-299 | Unassigned | |
| 300 | Multiple Choices | RFC 9110, Section 15.4.1 |
| 301 | Moved Permanently | RFC 9110, Section 15.4.2 |
| 302 | Found | RFC 9110, Section 15.4.3 |
| 303 | See Other | RFC 9110, Section 15.4.4 |
| 304 | Not Modified | RFC 9110, Section 15.4.5 |
| 305 | Use Proxy | RFC 9110, Section 15.4.6 |
| 306 | (Unused) | RFC 9110, Section 15.4.7 |
| 307 | Temporary Redirect | RFC 9110, Section 15.4.8 |
| 308 | Permanent Redirect | RFC 9110, Section 15.4.9 |
| 309-399 | Unassigned | |
| 400 | Bad Request | RFC 9110, Section 15.5.1 |
| 401 | Unauthorized | RFC 9110, Section 15.5.2 |
| 402 | Payment Required | RFC 9110, Section 15.5.3 |
| 403 | Forbidden | RFC 9110, Section 15.5.4 |
| 404 | Not Found | RFC 9110, Section 15.5.5 |
| 405 | Method Not Allowed | RFC 9110, Section 15.5.6 |
| 406 | Not Acceptable | RFC 9110, Section 15.5.7 |
| 407 | Proxy Authentication Required | RFC 9110, Section 15.5.8 |
| 408 | Request Timeout | RFC 9110, Section 15.5.9 |
| 409 | Conflict | RFC 9110, Section 15.5.10 |
| 410 | Gone | RFC 9110, Section 15.5.11 |
| 411 | Length Required | RFC 9110, Section 15.5.12 |
| 412 | Precondition Failed | RFC 9110, Section 15.5.13 |
| 413 | Content Too Large | RFC 9110, Section 15.5.14 |
| 414 | URI Too Long | RFC 9110, Section 15.5.15 |
| 415 | Unsupported Media Type | RFC 9110, Section 15.5.16 |
| 416 | Range Not Satisfiable | RFC 9110, Section 15.5.17 |
| 417 | Expectation Failed | RFC 9110, Section 15.5.18 |
| 418 | (Unused) | RFC 9110, Section 15.5.19 |
| 419-420 | Unassigned | |
| 421 | Misdirected Request | RFC 9110, Section 15.5.20 |
| 422 | Unprocessable Content | RFC 9110, Section 15.5.21 |
| 423 | Locked | RFC 4918 |
| 424 | Failed Dependency | RFC 4918 |
| 425 | Too Early | RFC 8470 |
| 426 | Upgrade Required | RFC 9110, Section 15.5.22 |
| 427 | Unassigned | |
| 428 | Precondition Required | RFC 6585 |
| 429 | Too Many Requests | RFC 6585 |
| 430 | Unassigned | |
| 431 | Request Header Fields Too Large | RFC 6585 |
| 432-450 | Unassigned | |
| 451 | Unavailable For Legal Reasons | RFC 7725 |
| 452-499 | Unassigned | |
| 500 | Internal Server Error | RFC 9110, Section 15.6.1 |
| 501 | Not Implemented | RFC 9110, Section 15.6.2 |
| 502 | Bad Gateway | RFC 9110, Section 15.6.3 |
| 503 | Service Unavailable | RFC 9110, Section 15.6.4 |
| 504 | Gateway Timeout | RFC 9110, Section 15.6.5 |
| 505 | HTTP Version Not Supported | RFC 9110, Section 15.6.6 |
| 506 | Variant Also Negotiates | RFC 2295 |
| 507 | Insufficient Storage | RFC 4918 |
| 508 | Loop Detected | RFC 5842 |
| 509 | Unassigned | |
| 510 | Not Extended (OBSOLETED) | RFC 2774; Status change of HTTP experiments to Historic |
| 511 | Network Authentication Required | RFC 6585 |
| 512-599 | Unassigned | |

---

Title: Коды состояния ответа HTTP - HTTP | MDN
URL: https://developer.mozilla.org/ru/docs/Web/HTTP/Reference/Status
Published: N/A
Author: 203 Non-Authoritative Information
Highlights:
Код состояния ответа HTTP показывает, был ли успешно выполнен определённый HTTP запрос. Ответы сгруппированы в 5 классов:

1. Информационные ответы (`100` – `199`)
2. Успешные ответы (`200` – `299`)
3. Сообщения о перенаправлении (`300` – `399`)
4. Ошибки клиента (`400` – `499`)
5. Ошибки сервера (`500` – `599`)

Коды состояния определены в RFC 9110.

...

`400 Bad Request`
: Сервер не может или не будет обрабатывать запрос из-за чего-то, что воспринимается как ошибка клиента (например, неправильный синтаксис, формат или маршрутизация запроса).
`401 Unauthorized`
: Хотя стандарт HTTP определяет этот ответ как «неавторизованный», семантически он означает «неаутентифицированный». Это значит, что клиент должен аутентифицировать себя, чтобы получить запрошенный ответ.
`402 Payment Required`
: Этот код ответа зарезервирован для использования в будущем. Первоначальной целью создания этого кода было использование его для цифровых платежных систем, однако он используется очень редко и стандартного соглашения не существует.
`403 Forbidden`
: Клиент не имеет прав доступа к контенту, то есть он неавторизован, поэтому сервер отказывается предоставить запрошенный ресурс. В отличие от `401 Unauthorized`, личность клиента известна серверу.
`404 Not Found`
: Сервер не может найти запрошенный ресурс. В браузере это означает, что URL-адрес не распознан. В API это также может означать, что адрес правильный, но ресурс не существует. Сервер также может отправить этот код ответа вместо `403 Forbidden`, чтобы скрыть существование ресурса от неавторизованного клиента. Это самый известный код ответа из-за его частого появления в сети.
`405 Method Not Allowed`
: Метод запроса известен серверу, но не поддерживается целевым ресурсом. Например, API может не разрешать вызов `DELETE` для удаления ресурса.
`406 Not Acceptable`
: Сервер после выполнения согласования контента не нашёл содержимого, соответствующего критериям, заданным пользовательским агентом.
`407 Proxy Authentication Required`
: Этот код ответа похож на `401 Unauthorized`, но аутентификация должна выполняться через прокси-сервер.
`408 Request Timeout`
: Сервер может отправить этот код ответа при неиспользовании соединения, даже без предварительного запроса со стороны клиента. Он означает, что сервер хотел бы закрыть это соединение. Этот ответ используется сравнительно часто, поскольку некоторые браузеры (такие как Chrome, Firefox 27+ или IE9) для ускорения используют механизмы предварительного подключения HTTP. Некоторые серверы просто закрывают соединение, не отправляя это сообщение.
`409 Conflict`
: Запрос конфликтует с текущим состоянием сервера.
`410 Gone`
: Запрошенное содержимое было удалено с сервера, и отсутствует возможность переадресации. Ожидается, что клиенты удалят свои кеши и ссылки на этот ресурс. Спецификация HTTP предполагает, что этот код ответа будет использоваться для «ограниченных по времени или рекламных услуг». API не обязаны указывать ресурсы, которые были удалены, с помощью этого кода.
`411 Length Required`
: Запрос отклонён, потому что сервер требует указание поля заголовка `Content-Length`, но оно не определено.
`412 Precondition Failed`
: Клиент указал в заголовках запроса условия, которым сервер не соответствует.
`413 Payload Too Large`
: Размер объекта запроса превышает ограничения, определенные сервером. Сервер может закрыть соединение или вернуть поле заголовка `Retry-After`.
`414 URI Too Long`
: Запрошенный клиентом URI слишком длинный для того, чтобы сервер смог его обработать.
`415 Unsupported Media Type`
: Запрос отклонён, потому что медиа формат запрашиваемых данных не поддерживается сервером.
`416 Range Not Satisfiable`
: Сервер не может корректно обработать запрос с учётом диапазона, указанного в поле заголовка `Range`.
`417 Expectation Failed`
: Сервер не может выполнить ожидание, указанное в поле заголовка запроса `Expect`.
`418 I'm a teapot`
: «Шуточный» ответ: сервер отклоняет попытку заварить кофе в чайнике.
`421 Misdirected Request`
: Сервер не может дать ответ. Возможно сервер не настроен для комбинации схемы и полномочий, указанных в URI запроса.
`422 Unprocessable Content` (WebDAV)
: Запрос сформирован правильно, но его невозможно выполнить из-за семантических ошибок.
`423 Locked` (WebDAV)
: Запрашиваемый ресурс заблокирован.
`424 Failed Dependency` (WebDAV)
: Запрос не выполнен из-за проблем в предыдущем запросе.
`425 Too Early`
: Клиент отправил порцию данных слишком рано, до того как сервер установил безопасное соединение.
`426 Upgrade Required`
: Сервер отказывается выполнять запрос с использованием текущего протокола, но может быть готов сделать это после смены протокола на указанный в заголовке ответа `Upgrade`.
`428 Precondition Required`
: Сервер требует, чтобы запрос содержал условия. Этот ответ предназначен для предотвращения проблемы одновременного изменения ресурса несколькими пользователями.
`429 Too Many Requests`
: Пользователь отправил слишком много запросов в определённый промежуток времени.
`431 Request Header Fields Too Large`
: Сервер не будет обрабатывать запрос, потому что поля заголовка слишком велики. Запрос может быть отправлен повторно после уменьшения размера полей заголовка.
`451 Unavailable For Legal Reasons`
: Пользовательский агент запросил ресурс, который не может быть предоставлен по закону, например веб-страницу, подвергнутую цензуре со стороны правительства.

---

Title: RFC 9110: HTTP Semantics
URL: https://www.rfc-editor.org/rfc/rfc9110.pdf
Published: N/A
Author: Roy T. Fielding, Mark Nottingham, Julian Reschke
Highlights:
## RFC 9110 HTTP Semantics

### Abstract

The Hypertext Transfer Protocol (HTTP) is a stateless application-level protocol for distributed, 
collaborative, hypertext information systems. This document describes the overall architecture 
of HTTP, establishes common terminology, and defines aspects of the protocol that are shared by 
all versions. In this definition are core protocol elements, extensibility mechanisms, and the 
"http" and "https" Uniform Resource Identifier (URI) schemes. 
This document updates RFC 3864 and obsoletes RFCs 2818, 7231, 7232, 7233, 7235, 7538, 7615, 7694, 
and portions of 7230. 
Stream: 
RFC: 
STD: 
Obsoletes: 
Updates: 
Category: 
Published: 
ISSN: 
Authors: 
Internet Engineering Task Force (IETF) 
9110 
97 
2818, 7230, 7231, 7232, 7233, 7235, 7538, 7615, 7694 
3864 
Standards Track 
June 2022 
2070-1721 
R. Fielding, Ed. 
Adobe

...

### Status of This Memo

This is an Internet Standards Track document. 
This document is a product of the Internet Engineering Task Force (IETF). It represents the 
consensus of the IETF community. It has received public review and has been approved for 
publication by the Internet Engineering Steering Group (IESG). Further information on Internet 
Standards is available in Section 2 of RFC 7841. 
Information about the current status of this document, any errata, and how to provide feedback 
on it may be obtained at https://www.rfc-editor.org/info/rfc9110.

...

Message Abstraction 6.1.  Framing and Completeness 6.2. ... Content Semantics 6.4.2. ... Trailer Fields 6.5.1. ... Processing Trailer Fields 6.6.  Message Metadata 6.6.1.  Date 6.6.2.

...

7.  Routing HTTP Messages 7.1.  Determining the Target Resource 7.2.  Host and :authority 7.3.  Routing Inbound Requests 7.3.1.  To a Cache 7.3.2.  To a Proxy 7.3.3.  To the Origin 7.4.  Rejecting Misdirected Requests 7.5.  Response Correlation 7.6.  Message Forwarding 7.6.1.  Connection 7.6.2.  Max-Forwards 7.6.3.  Via 7.7.  Message Transformations

...

15.4.2.  301 Moved Permanently 15.4.3.  302 Found 15.4.4.  303 See Other 15.4.5.  304 Not Modified 15.4.6.  305 Use Proxy 15.4.7.  306 (Unused) 15.4.8.  307 Temporary Redirect 15.4.9.  308 Permanent Redirect 15.5.  Client Error 4xx 15.5.1.  400 Bad Request 15.5.2.  401 Unauthorized 15.5.3.  402 Payment Required 15.5.4.  403 Forbidden 15.5.5.  404 Not Found 15.5.6.  405 Method Not Allowed 15.5.7.  406 Not Acceptable 15.5.8.  407 Proxy Authentication Required 15.5.9.  408 Request Timeout 15.5.10. 409 Conflict 15.5.11. 410 Gone 15.5.12. 411 Length Required 15.5.13. 412 Precondition Failed 15.5.14. 413 Content Too Large 15.5.15. 414 URI Too Long 15.5.16. 415 Unsupported Media Type 15.5.17. 416 Range Not Satisfiable 15.5.18. 417 Expectation Failed 15.5.19. 418 (Unused) 15.5.20. 421 Misdirected Request 15.5.21. 422 Unprocessable Content

---

Title: 421 Misdirected Request - HTTP | MDN
URL: https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Status/421
Published: N/A
Author: N/A
Highlights:
# 421 Misdirected Request

The HTTP `421 Misdirected Request` client error response status code indicates that the request was directed to a server that is not able to produce a response. This can be sent by a server that is not configured to produce responses for the combination of scheme and authority that are included in the request URI.

Clients may retry the request over a different connection.

## Status

http

```
421 Misdirected Request

```

---

Title: 421 Misdirected Request - HTTP status code explained
URL: https://http.dev/421
Published: N/A
Author: Fili
Highlights:
# 421 Misdirected Request

When a request arrives on a connection not intended for the target server, the response is 421 Misdirected Request. Originally defined in HTTP/2, this status is now part of general HTTP semantics.

...

The 421 Misdirected Request error indicates the server is unable to produce an authoritative response for the target URL. This status is sent as a result of connection reuse, where a request for one host arrives on a connection established with a different host. In response, a client tries to resubmit the request over a different connection.

---

Title: Коды состояния HTTP | Integration Helper
URL: https://greymiller13.github.io/integration-helper/http/status-codes
Published: N/A
Author: N/A
Highlights:
| Код | Название | Краткий смысл | Стандарт |
| --- | --- | --- | --- |
| 100 | Continue | Заголовки приняты, можно отправлять тело | RFC 9110 |
| 101 | Switching Protocols | Переход на другой протокол (WebSocket) | RFC 9110 |
| 102 | Processing | Сервер ещё обрабатывает запрос (устарел) | RFC 2518 |
| 103 | Early Hints | Предварительные заголовки для подгрузки ресурсов | RFC 8297 |
| 104 | Upload Resumption Supported | Сервер поддерживает возобновляемую загрузку | Черновик IETF (временная регистрация) |
| 200 | OK | Успех | RFC 9110 |
| 201 | Created | Ресурс создан | RFC 9110 |
| 202 | Accepted | Принято к асинхронной обработке | RFC 9110 |
| 203 | Non-Authoritative Information | Ответ изменён прокси | RFC 9110 |
| 204 | No Content | Успех, тела нет | RFC 9110 |
| 205 | Reset Content | Успех, сбросить форму | RFC 9110 |
| 206 | Partial Content | Отдана часть ресурса (Range) | RFC 9110 |
| 207 | Multi-Status | Несколько статусов в теле | RFC 4918 |
| 208 | Already Reported | Элемент уже перечислен выше | RFC 5842 |
| 226 | IM Used | Отдана дельта изменений | RFC 3229 |
| 300 | Multiple Choices | Несколько вариантов представления | RFC 9110 |
| 301 | Moved Permanently | Ресурс переехал навсегда | RFC 9110 |
| 302 | Found | Временно по другому адресу | RFC 9110 |
| 303 | See Other | Результат — по другому адресу, запрашивать `GET` | RFC 9110 |
| 304 | Not Modified | Не изменился, используйте кэш | RFC 9110 |
| 305 | Use Proxy | Использовать прокси (устарел) | RFC 9110 |
| 306 | (Unused) | Зарезервирован, не используется | RFC 9110 |
| 307 | Temporary Redirect | Временно по другому адресу, метод сохраняется | RFC 9110 |
| 308 | Permanent Redirect | Переехал навсегда, метод сохраняется | RFC 9110 |
| 400 | Bad Request | Некорректный запрос | RFC 9110 |
| 401 | Unauthorized | Не аутентифицирован | RFC 9110 |
| 402 | Payment Required | Зарезервирован для оплаты | RFC 9110 |
| 403 | Forbidden | Доступ запрещён | RFC 9110 |
| 404 | Not Found | Ресурс не найден | RFC 9110 |
| 405 | Method Not Allowed | Метод не поддерживается ресурсом | RFC 9110 |
| 406 | Not Acceptable | Нет представления в запрошенном формате | RFC 9110 |
| 407 | Proxy Authentication Required | Нужна аутентификация на прокси | RFC 9110 |
| 408 | Request Timeout | Клиент не успел отправить запрос | RFC 9110 |
| 409 | Conflict | Конфликт с текущим состоянием ресурса | RFC 9110 |
| 410 | Gone | Ресурс удалён навсегда | RFC 9110 |
| 411 | Length Required | Нужен `Content-Length` | RFC 9110 |
| 412 | Precondition Failed | Не выполнено условие (`If-Match` и др.) | RFC 9110 |
| 413 | Content Too Large | Тело запроса слишком велико | RFC 9110 |
| 414 | URI Too Long | Слишком длинный URI | RFC 9110 |
| 415 | Unsupported Media Type | Формат тела не поддерживается | RFC 9110 |
| 416 | Range Not Satisfiable | Запрошенный диапазон недоступен | RFC 9110 |
| 417 | Expectation Failed | Не выполнено ожидание `Expect` | RFC 9110 |
| 418 | (Unused) | «I'm a teapot», зарезервирован | RFC 9110, RFC 2324 |
| 421 | Misdirected Request | Запрос попал не на тот сервер | RFC 9110 |
| 422 | Unprocessable Content | Синтаксис верен, но данные не обработать | RFC 9110 |
| 423 | Locked | Ресурс заблокирован | RFC 4918 |
| 424 | Failed Dependency | Не выполнена зависимая операция | RFC 4918 |
| 425 | Too Early | Риск повторного воспроизведения (0-RTT) | RFC 8470 |
| 426 | Upgrade Required | Нужно перейти на другой протокол | RFC 9110 |
| 428 | Precondition Required | Требуется условный запрос | RFC 6585 |
| 429 | Too Many Requests | Превышен лимит запросов | RFC 6585 |
| 431 | Request Header Fields Too Large | Слишком большие заголовки | RFC 6585 |
| 451 | Unavailable For Legal Reasons | Недоступно по юридическим причинам | RFC 7725 |
| 500 | Internal Server Error | Внутренняя ошибка сервера | RFC 9110 |
| 501 | Not Implemented | Функциональность не реализована | RFC 9110 |
| 502 | Bad Gateway | Шлюз получил некорректный ответ | RFC 9110 |
| 503 | Service Unavailable | Сервис временно недоступен | RFC 9110 |
| 504 | Gateway Timeout | Шлюз не дождался ответа | RFC 9110 |
| 505 | HTTP Version Not Supported | Версия HTTP не поддерживается | RFC 9110 |
| 506 | Variant Also Negotiates | Ошибка конфигурации согласования | RFC 2295 |
| 507 | Insufficient Storage | Недостаточно места для хранения | RFC 4918 |
| 508 | Loop Detected | Обнаружен бесконечный цикл | RFC 5842 |
| 510 | Not Extended | Нужны расширения запроса (исторический) | RFC 2774 |
| 511 | Network Authentication Required | Нужна аутентификация в сети | RFC 6585 |

...

### 421 Misdirected Request ​

Запрос направлен на сервер, который не может ответить для указанной комбинации схемы и authority. Появился в HTTP/2 (RFC 7540), теперь в RFC 9110.

Типичная причина — повторное использование соединения (connection coalescing): клиент отправил запрос к `b.example.com` по соединению, открытому для `a.example.com` (общий IP и wildcard-сертификат), а сервер обслуживает эти домены раздельно. Клиент может повторить запрос в новом соединении, даже если метод неидемпотентный.

---

Title: HTTP 421 Misdirected Request — Meaning & Status Code Reference
URL: https://errorlookup.com/status/421/
Published: N/A
Author: N/A
Highlights:
HTTP 421 Misdirected Request means the server that received the request is not able or willing to produce an authoritative response for the target URI. This is primarily an HTTP/2 issue, where connection reuse across multiple hostnames can result in requests being delivered to a server that does not handle that hostname.

...

## Quick reference

| Code | 421 |
| --- | --- |
| Name | Misdirected Request |
| Category | 4xx Client Errors |
| Specification | RFC 9110 §15.5.20 |
| IANA status | Assigned |
| Cacheable | No |
| Client action | Retry the request over a new connection. The current connection cannot serve this host. |
| In-depth guide | HTTP 421 full guide → |

...

RFC 9110 defines 421 as indicating that the request was directed at a server that is not able to produce a response for that combination of scheme and authority. The server is essentially saying: this request was delivered to the wrong server, and I cannot authoritatively handle it.

---

Title: 421 Misdirected Request
URL: https://evertpot.com/http/421-misdirected-request
Published: 2019-04-16T08:20:26.000Z
Author: N/A
Highlights:
421 Misdirected Request

April 16, 2019

# 421 Misdirected Request

A server should emit `421 Misdirected Request` when it receives a HTTP request that was not intended for that server.

This status was introduced with HTTP/2, but it may also be applicable to HTTP/1 servers. For example, a server might receive the following HTTP request:

```
GET /contact.html HTTP/1.1
Host: foo.example.org

```

Since HTTP/1.1 a client is required to include a `Host` header. A server might already know that the `foo.example.org` domain is not configured on that server, cand could respond with a `421 Misdirected Request` response to tell the client that it connected to the wrong server:

```
HTTP/1.1 421 Misdirected Request
Content-Type: text/html

<h1>Switchboard operator error</h1>

```

So when can that actually happen? One example of this is that the DNS for a server was set to the wrong IP or CNAME, or simply a server configuration error.

## HTTP/2

There’s other examples where this might occur. In HTTP/2 it will be possible for a single HTTP/2 connection to be used for multiple domainnames via connection coalescing.

If a client is trying to use this feature but a server doesn’t support it, it must return `421 Misdirected Request` This is actually the real reason this status got introduced.

## References

- RFC7540, Section 9.1.2 - 412 Misdirected Request

---

Title: Update HttpStatus to align with RFC9110 where relevant
URL: https://github.com/spring-projects/spring-framework/issues/32870
Published: N/A
Author: N/A
Highlights:
**Affects:** 6.1 
 
The `HttpStatus` javadoc links to HTTP Status Code Registry, which in turn refers to RFC9110 (published in June 2022). However the detailed documentation for `HttpStatus`’s values still refer to RFC7231, which was obsoleted by the former. 
 
Some statuses have been updated. In particular, statuses 421 & 422 which used to be part of WebDav are now part of this RFC. I didn’t check for all statuses or other usages in the documentation.

...

**simonbasle** commented on 2024-05-28T12:35:52Z:

> Other changes that I could spot looking at https://www.iana.org/assignments/http-status-codes/http-status-codes.xhtml are:
> * `413`: `PAYLOAD_TOO_LARGE` becomes `CONTENT_TOO_LARGE` with slight variations in wording around protocols that allow request termination instead of connection close
> * `421`: new `MISDIRECT_REQUEST` (we do have a deprecated enum value for the WebDAV code)
> * `422`: `UNPROCESSABLE_ENTITY` becomes `UNPROCESSABLE_CONTENT`
> * `509`: `BANDWIDTH_LIMIT_EXCEEDED` seems to now be Unassigned
> * `510`: `NOT_EXTENDED` obsoleted (RFC2774 moved to Historic)

---

Title: 421 Misdirected Request - HTTP Status Code
URL: https://httperrors.com/status/421-misdirected-request
Published: N/A
Author: N/A
Highlights:
421 Misdirected Request - HTTP Status Code

# Status Code 421

## Misdirected Request

The request was directed at a server that is not able to produce a response.

#### Category

Client Error

#### Spec URL

421 of RFC 9110 

#### Popularity

rare

#### Recommended

No

#### Deprecated

#### Common Use Case

HTTP/2 connection reuse issues

#### Notes

Used to indicate that a request was sent to the wrong server.

#### RFC Reference

RFC 9110 HTTP/1.1 (2022)

Defines the HTTP/1.1 protocol, including semantics, caching, and connection management.

#### Description

The request was directed at a server that is not able to produce a response.

...

The normative anchor here is RFC 9110, with a direct reference at https://datatracker.ietf.org/doc/html/rfc9110#section-15.5.19. That RFC context matters because the exact words in the standard often settle edge cases around caching, retries, authentication, payload requirements, or intermediary behavior.
=== END OF OUTPUT X48 ===

=== OUTPUT D37 ===
**Ответ: код 421.** Он означает, что запрос адресован серверу, который не может сформировать ответ для данной комбинации схемы и authority из URI. Оригинально он определён в RFC 7540 (HTTP/2), раздел 9.1.2. Сейчас код является частью общей семантики HTTP, то есть актуальное определение находится в RFC 9110 (HTTP Semantics). Номер раздела в RFC 9110 (15.5.20) я называю по собственным знаниям, поиск его не подтвердил.

Поиск также показал, что клиент, получивший 421, может повторить запрос по другому соединению. Обычно это связано с повторным использованием HTTP/2-соединения (connection coalescing) для нескольких доменов.

Sources:
1. https://http.dev/421
2. https://wheregoes.com/http-status-codes/421/
3. https://apidog.com/vi/blog/status-code-421-misdirected-request/
4. https://apidog.com/blog/status-code-421-misdirected-request
5. https://server.hk/blog/15193
6. https://http.devtool.tech/421
7. https://enterno.io/en/status-codes/421-misdirected-request
=== END OF OUTPUT D37 ===

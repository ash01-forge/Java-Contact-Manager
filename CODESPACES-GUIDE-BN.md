# ব্রাউজারে আসল Java Contact Manager চালানো

এটি তোমার Java Swing app-ই চালাবে। GitHub Codespaces-এর Linux computer-এ Java চলবে এবং noVNC দিয়ে ব্রাউজারে সেই desktop দেখা যাবে।

## ১. নতুন package upload

ZIP-টি Extract All করো। Java-Contact-Manager ফোল্ডারের ভেতরের সবকিছু repository-তে upload করতে হবে। বিশেষ করে .devcontainer, .vscode, scripts ও src যেন থাকে। ZIP ফাইলটিকে একমাত্র file হিসেবে upload করবে না।

Repository-তে আগে পুরোনো package দিলে এই নতুন setup-এর ফাইলগুলো যোগ করো। .gitignore, .gitattributes ও README.md-এর নতুন সংস্করণও রাখতে হবে।

## ২. Codespace তৈরি

Repository খোলো → সবুজ Code বাটন → Codespaces → Create codespace on main। তোমার default branch-এর নাম আলাদা হলে সেটির নাম দেখাবে। প্রথমবার desktop environment তৈরি হতে কিছু সময় লাগবে।

আগে তৈরি Codespace থাকলে upload করা নতুন ফাইলগুলো সেখানে sync করতে হবে, তারপর Ctrl+Shift+P → Codespaces: Rebuild Container। নতুন Codespace তৈরি করাই সহজ।

## ৩. App দেখা

সেটআপ শেষে editor-এর নিচের PORTS tab খোলো। 6080 — Java Contact Manager Desktop খুঁজে দেখো। Visibility Private রাখো। তারপর ওই সারির globe/Open in Browser চাপো।

noVNC পেজে Connect চাপো। Desktop password: vscode

এটি GitHub account-এর password নয়। Private desktop-এর default password।

Java app-এর welcome screen দেখা গেলে Start চাপো। এবার Add, Search, View ও Delete ব্যবহার করতে পারবে। Demo-তে fictional contact ব্যবহার করো।

## ৪. App window না এলে

Codespaces editor-এ Terminal → Run Task → Contact Manager: Open app নির্বাচন করো। অথবা সেখানকার terminal-এ চালাও:

```text
python3 scripts/run.py --background
```

সমস্যা থাকলে build/app.log খোলো। 6080 port না দেখালে PORTS → Add port-এ 6080 দাও। DISPLAY বা desktop service-এর সমস্যা থাকলে Rebuild Container করো। GitHub-এর build log/screenshot দেখে প্রয়োজনে আরও ঠিক করা যাবে।

## ৫. কাজ শেষে

https://github.com/codespaces থেকে ওই Codespace-এর menu → Stop codespace। Browser tab বন্ধ করা আর Codespace Stop করা একই কাজ নয়। একই Codespace resume করলে workspace ও data থাকে; Codespace Delete করলে স্থানীয় data-ও চলে যেতে পারে।

Codespaces-এর compute ও storage quota আছে। Payment method না থাকলে quota শেষ হলে ব্যবহার থেমে যায়; payment enabled থাকলে খরচ account budget-এর ওপর নির্ভর করে।

## LinkedIn-এ কোন link দেবে

Repository link দেবে। Desktop-এর Private session link-কে সবার ব্যবহারের public demo হিসেবে দেবে না। README-তে অন্যরা নিজের Codespace তৈরি করার পদ্ধতি পাবে।

## যাচাইয়ের সীমা

Java source compile ও local contact-storage test আগে পাস করেছে। নতুন launcher দিয়ে Java compilation, Python syntax, configuration-এর file path/port এবং .gitignore নিয়ম স্থানীয়ভাবে যাচাই হয়েছে। এটি live container build বা GUI test নয়। আসল GitHub Codespace এখনও তৈরি হয়নি; cloud build, noVNC connection ও GUI operation সেখানে পরীক্ষা করতে হবে।

## অফিসিয়াল নির্দেশনা

- https://github.com/devcontainers/features/blob/main/src/desktop-lite/README.md
- https://docs.github.com/en/codespaces/developing-in-a-codespace/forwarding-ports-in-your-codespace
- https://docs.github.com/en/billing/concepts/product-billing/github-codespaces

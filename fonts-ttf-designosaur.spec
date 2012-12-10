%define pkgname designosaur

Summary:	Designosaur font family
Name:		fonts-ttf-designosaur
Version:	20110526
Release:	1
License:	Creative Commons Attribution
Group:		System/Fonts/True type
URL:		http://openfontlibrary.org/font/designosaur
Source0:	%{pkgname}.zip
BuildArch:	noarch
BuildRequires:	freetype-tools

%description
"Designosaur" typeface was inspired by classic school design canons to turn
greatly elegant and functional, serve for various ideas and survive decades.

%prep
%setup -q -c -n %{name}-%{version}

%build

%install
%__rm -rf %{buildroot}

%__mkdir_p %{buildroot}%{_xfontdir}/TTF/designosaur

%__install -m 644 OT-tt/*.ttf %{buildroot}%{_xfontdir}/TTF/designosaur
ttmkfdir %{buildroot}%{_xfontdir}/TTF/designosaur -o %{buildroot}%{_xfontdir}/TTF/designosaur/fonts.dir
%__ln_s fonts.dir %{buildroot}%{_xfontdir}/TTF/designosaur/fonts.scale

%__mkdir_p %{buildroot}%_sysconfdir/X11/fontpath.d/
%__ln_s ../../..%{_xfontdir}/TTF/designosaur \
    %{buildroot}%_sysconfdir/X11/fontpath.d/ttf-designosaur:pri=50

%__install -d %{buildroot}%{_docdir}/%{name}
cat > %{buildroot}%{_docdir}/%{name}/README << EOF
Family		Designosaur
Designer	Sergiy S. Tkachenko 
Foundry		Sergiy S. Tkachenko 
License		CC-BY
Category	Serif

Description

"Designosaur" typeface was inspired by classic school design canons to turn
greatly elegant and functional, serve for various ideas and survive decades.

Full Language Support

Afrikaans, Baltic, Basic Cyrillic, Basic Latin, Catalan, Central European,
Dutch, Euro, Igbo Onwu, Pinyin, Romanian, Turkish, Vietnamese, Western
European.
EOF

%files
%doc %{_docdir}/%{name}/README
%dir %{_xfontdir}/TTF/designosaur
%{_xfontdir}/TTF/designosaur/*.ttf
%verify(not mtime) %{_datadir}/fonts/TTF/designosaur/fonts.dir
%{_xfontdir}/TTF/designosaur/fonts.scale
%{_sysconfdir}/X11/fontpath.d/ttf-designosaur:pri=50


%changelog
* Wed Dec 14 2011 Dmitry Mikhirev <dmikhirev@mandriva.org> 20110526-1
+ Revision: 741139
- imported package fonts-ttf-designosaur


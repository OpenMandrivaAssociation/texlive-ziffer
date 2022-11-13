Name:		texlive-ziffer
Version:	32279
Release:	1
Summary:	Conversion of punctuation in maths mode
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/ziffer
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/ziffer.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/ziffer.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The package modifies the behaviour of characters in maths mode
so that: '.' is used as a one-thousand separator (as is common
in Germany) ',' is used as a decimal separator (as is common in
Germany) '--' is represented with spacing as appropriate to
such constructs as '1.000,--'. These conversions may be
switched on and off.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/ziffer/ziffer.sty
%doc %{_texmfdistdir}/doc/latex/ziffer/README

#-----------------------------------------------------------------------
%prep
%autosetup -p1 -c -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}

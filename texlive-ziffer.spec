# revision 32279
# category Package
# catalog-ctan /macros/latex/contrib/ziffer
# catalog-date 2012-05-09 18:20:59 +0200
# catalog-license lppl
# catalog-version 2.1
Name:		texlive-ziffer
Version:	2.1
Release:	12
Summary:	Conversion of punctuation in maths mode
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/ziffer
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/ziffer.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/ziffer.doc.tar.xz
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
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}

%global tl_name ziffer
%global tl_revision 79618

Name:		texlive-%{tl_name}
Epoch:		1
Version:	2.1
Release:	%{tl_revision}.1
Summary:	Conversion of punctuation in maths mode
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/ziffer
License:	lppl1.3c
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/ziffer.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/ziffer.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The package modifies the behaviour of characters in maths mode so that:
'.' is used as a one-thousand separator (as is common in Germany) ',' is
used as a decimal separator (as is common in Germany) '--' is
represented with spacing as appropriate to such constructs as
'1.000,--'. These conversions may be switched on and off.


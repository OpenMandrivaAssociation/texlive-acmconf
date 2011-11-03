# revision 15878
# category Package
# catalog-ctan /macros/latex/contrib/acmconf
# catalog-date 2008-05-14 19:23:34 +0200
# catalog-license lppl
# catalog-version 1.3
Name:		texlive-acmconf
Version:	1.3
Release:	1
Summary:	Class for ACM conference proceedings
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/acmconf
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/acmconf.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/acmconf.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/acmconf.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(post):	texlive-tlpkg
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3
Conflicts:	texlive-source <= 20110705-3

%description
This class may be used to typeset articles to be published in
the proceedings of ACM (Association for Computing Machinery)
conferences and workshops. The layout produced by the acmconf
class is based on the ACM's own specification.

%pre
    %_texmf_mktexlsr_pre

%post
    %_texmf_mktexlsr_post

%preun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_pre
    fi

%postun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/acmconf/acmconf.cls
%doc %{_texmfdistdir}/doc/latex/acmconf/README
%doc %{_texmfdistdir}/doc/latex/acmconf/THIS-IS-VERSION-1.3
%doc %{_texmfdistdir}/doc/latex/acmconf/accept.tex
%doc %{_texmfdistdir}/doc/latex/acmconf/acmconf.pdf
%doc %{_texmfdistdir}/doc/latex/acmconf/body.eps
%doc %{_texmfdistdir}/doc/latex/acmconf/error.tex
%doc %{_texmfdistdir}/doc/latex/acmconf/prepare.tex
%doc %{_texmfdistdir}/doc/latex/acmconf/print.tex
%doc %{_texmfdistdir}/doc/latex/acmconf/pubform.bib
%doc %{_texmfdistdir}/doc/latex/acmconf/pubform.tex
%doc %{_texmfdistdir}/doc/latex/acmconf/publish.tex
%doc %{_texmfdistdir}/doc/latex/acmconf/submit.tex
#- source
%doc %{_texmfdistdir}/source/latex/acmconf/Makefile
%doc %{_texmfdistdir}/source/latex/acmconf/acmconf.dtx
%doc %{_texmfdistdir}/source/latex/acmconf/acmconf.ins
%doc %{_tlpkgobjdir}/*.tlpobj

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
mkdir -p %{buildroot}%{_tlpkgobjdir}
cp -fpa tlpkg/tlpobj/*.tlpobj %{buildroot}%{_tlpkgobjdir}
